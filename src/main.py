from flask import Flask, request, jsonify, render_template, abort, session, redirect, flash
from flask_session import Session
import backendfunctions as bf

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
        return render_template('signup.html')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    isteacher = True if request.form.get('selectedtoggle') == "teacher" else False

    res = bf.signup(bf.create_connection(), name, email, password, repassword, isteacher)
    if res is None:
        abort(500)

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
    return render_template('teacher/page2.html', assignments=assignments, coursename=bf.get_course_name(bf.create_connection(), courseid))

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
        res = bf.add_question_to_assignment(bf.create_connection(), assignmentid, question[0], question[1])
        if res is None:
            abort(500)

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
    assignments = bf.get_assignments(bf.create_connection(), courseid)
    return render_template('student/page2.html', assignments=assignments, coursename=bf.get_course_name(bf.create_connection(), courseid))

@app.route("/student/assignment/<int:assignmentid>", methods=['GET','POST'])
def student_assignment(assignmentid):
    if session.get("isteacher"):
        return redirect('/')
    if request.method == 'GET':
        questions = bf.get_questions(bf.create_connection(), assignmentid)
        return render_template('student/page3.html', questions=questions, assignmentid=assignmentid)
    answers = request.json
    for answer in answers:
        res = bf.make_submission(bf.create_connection(), answer[0], session.get("userid"), answer[1])
        if res is None:
            abort(500)
    return redirect(f'/student/dashboard')

if __name__ == '__main__':
    app.run(debug=True)