from flask import Flask, request, jsonify, render_template, abort, session, redirect, flash, send_from_directory
from flask_session import Session
import backendfunctions as bf
from nlp.grader import grader
import json

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = "asdoiu8013uKHDBF91"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if session.get("userid") is not None:
            if session.get("isteacher"):
                return redirect('/teacher/dashboard')
            return redirect('/student/dashboard')
        return render_template('login.html')
    
    email = request.form.get('email')
    password = request.form.get('password')

    res = bf.login(bf.create_connection(), email, password)
    if res is None:
        flash("Invalid email or password")
        return redirect('/login')
    
    session["userid"] = res[0]
    session["isteacher"] = res[1]
    session["name"] = res[2]

    if session["isteacher"]:
        return redirect('/teacher/dashboard')
    return redirect('/student/dashboard')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        if session.get("userid") is not None:
            if session.get("isteacher"):
                return redirect('/teacher/dashboard')
            return redirect('/student/dashboard')
        return render_template('signup.html')
    name = request.form.get('name')
    name = name.title()
    email = request.form.get('email')
    if not email.endswith("@dubai.bits-pilani.ac.in"):
        flash("Invalid email, use a BITS Dubai email")
        return redirect('/signup')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    isteacher = True if request.form.get('selectedtoggle') == "teacher" else False

    res = bf.signup(bf.create_connection(), name, email, password, repassword, isteacher)
    if res is None:
        flash("Invalid signup details")
        return redirect('/signup')

    session["userid"] = res
    session["isteacher"] = isteacher
    session["name"] = name

    if isteacher:
        return redirect('/teacher/dashboard')
    return redirect('/student/dashboard')

@app.route("/teacher/dashboard")
def teacher_home():
    if not session.get("isteacher"):
        return redirect('/')
    courses = bf.get_courses(bf.create_connection(), session.get("userid"))
    return render_template('teacher/index.html', courses=courses)

@app.route("/teacher/course/<int:courseid>")
def teacher_course(courseid):
    if not session.get("isteacher"):
        return redirect('/')
    assignments = bf.get_assignments(bf.create_connection(), courseid)
    return render_template('teacher/page2.html', assignments=assignments, coursename=bf.get_course_name(bf.create_connection(), courseid), courseid=courseid)

@app.route("/teacher/addquestion/<int:assignmentid>", methods=['GET','POST'])
def teacher_addquestion(assignmentid):
    if not session.get("isteacher"):
        return redirect('/')
    if request.method == 'GET':
        assigmentdetails = bf.get_assignment_details(bf.create_connection(), assignmentid)
        questions = bf.get_questions(bf.create_connection(), assignmentid)
        return render_template('teacher/page3.html', assignmentname=assigmentdetails[0], coursename=bf.get_course_name(bf.create_connection(), assigmentdetails[1]), assignmentid=assignmentid, questions=questions)
    questions = request.json
    bf.delete_all_questions(bf.create_connection(), assignmentid)
    for question in questions:
        res = bf.add_question_to_assignment(bf.create_connection(), assignmentid, question[0], question[1], question[2])
        if res is None:
            flash("Something went wrong")
            return redirect(f'/teacher/addquestion/{assignmentid}')

    return redirect(f'/teacher/dashboard')

@app.route("/student/dashboard")
def student_home():
    if session.get("isteacher"):
        return redirect('/')
    courses = bf.get_student_courses(bf.create_connection(), session.get("userid"))
    return render_template('student/index.html', courses=courses)

@app.route("/student/course/<int:courseid>")
def student_course(courseid):
    if session.get("isteacher"):
        return redirect('/')
    incompleteassignments = bf.get_incomplete_assignments(bf.create_connection(), courseid, session.get("userid"))
    completeassignments = bf.get_completed_assignments(bf.create_connection(), courseid, session.get("userid"))
    return render_template('student/page2.html', incompleteassignments=incompleteassignments, completeassignments=completeassignments, coursename=bf.get_course_name(bf.create_connection(), courseid), courseid=courseid)

@app.route("/getreportdyn/<int:assignmentid>", methods=['GET'])
def getreportdyn(assignmentid):
    if session.get("isteacher"):
        return redirect('/')
    #todo get all datas and return a report
    submissions = bf.get_submissions(bf.create_connection(), assignmentid, session.get("userid"))
    # return jsonify(submissions)
    student_name = session.get("name")
    teacher_name = bf.get_teacher_name(bf.create_connection(), assignmentid)
    submissions = {"submissions":submissions}
    submissions["Final Grade"] = f'{round(sum([submission[1]["Final Grade"] for submission in submissions["submissions"]])/len(submissions["submissions"]),2) }/{sum([submission[1]["Max Score"] for submission in submissions["submissions"]])}'
    return render_template("student/grading.html", submissions=submissions, student_name=student_name, teacher_name=teacher_name)

@app.route("/student/assignment/<int:assignmentid>", methods=['GET','POST'])
def student_assignment(assignmentid):
    if session.get("isteacher"):
        return redirect('/')
    if request.method == 'GET':
        questions = bf.get_questions(bf.create_connection(), assignmentid)
        assignment = bf.get_assignment_details(bf.create_connection(), assignmentid)
        return render_template('student/page3.html', questions=questions, assignmentid=assignmentid, assignmentname=assignment[0], coursename=bf.get_course_name(bf.create_connection(), assignment[1]))
    answers = request.json
    for answer in answers:
        res = bf.make_submission(bf.create_connection(), answer[0], session.get("userid"), answer[1])
        if res is None:
            flash("Something went wrong")
            return redirect(f'/student/assignment/{assignmentid}')
        question = bf.get_question(bf.create_connection(), answer[0])
        data = grader(question[0], question[1], answer[1], question[2])
        res2 = bf.store_report_data(bf.create_connection(), res, json.dumps(data), data["Final Grade"])
        if res2 is None:
            flash("Something went wrong")
            return redirect(f'/student/assignment/{assignmentid}')
    return redirect(f'/student/dashboard')

@app.route("/reportpath/<path:path>")
def path(path):
    return send_from_directory('static/data', path)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.route("/dashboard")
def dashboard():
    if session.get("isteacher"):
        return redirect('/teacher/dashboard')
    return redirect('/student/dashboard')

@app.route("/teacher/addcourse", methods=['POST'])
def addcourse():
    if not session.get("isteacher"):
        return redirect('/')
    coursename = request.form.get('coursename')
    res = bf.add_course(bf.create_connection(), session.get("userid"), coursename)
    if res is None:
        flash("Something went wrong")
    return redirect('/teacher/dashboard')

@app.route("/teacher/addassignment/<int:courseid>", methods=['POST'])
def addassignment(courseid):
    if not session.get("isteacher"):
        return redirect('/')
    assignmentname = request.form.get('assignmentname')
    section = request.form.get('section')
    duedate = request.form.get('duedate')
    res = bf.add_assignment(bf.create_connection(), courseid, assignmentname, section, duedate)
    if res is None:
        flash("Something went wrong")
    return redirect(f'/teacher/course/{courseid}')

@app.route("/teacher/students/<int:courseid>")
def students(courseid):
    if not session.get("isteacher"):
        return redirect('/')
    students = bf.get_students(bf.create_connection(), courseid)
    return render_template('teacher/studentlistcourse.html', students=students, coursename=bf.get_course_name(bf.create_connection(), courseid), courseid=courseid)

@app.route("/teacher/addstudent/<int:courseid>", methods=['POST'])
def addstudent(courseid):
    if not session.get("isteacher"):
        return redirect('/')
    studentemail = request.form.get('studentemail')
    uid = bf.get_student_user_id(bf.create_connection(), studentemail)
    if uid is None:
        flash("Student not found")
        return redirect(f'/teacher/students/{courseid}')
    res = bf.add_student_to_course(bf.create_connection(), uid, courseid)
    if res is None:
        flash("Something went wrong")
    return redirect(f'/teacher/students/{courseid}')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)