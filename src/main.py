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

    if isteacher:
        return redirect('/teacher/dashboard')
    return redirect('/student/dashboard')

@app.route("/teacher/dashboard")
def teacher_home():
    if not session.get("isteacher"):
        return redirect('/')
    return render_template('teacher/index.html')

@app.route("/student/dashboard")
def student_home():
    if session.get("isteacher"):
        return redirect('/')
    return render_template('student/index.html')

@app.route("/student/page2")
def student_page2():
    return render_template('student/page2.html')

if __name__ == '__main__':
    app.run(debug=True)