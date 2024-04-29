from flask import Flask, request, jsonify, render_template, abort

app = Flask(__name__)

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

    abort(500)

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    teacher_or_student = request.form.get('selectedtoggle')

    abort(500)

@app.route("/teacher/dashboard")
def teacher_home():
    return render_template('teacher/index.html')

@app.route("/student/dashboard")
def student_home():
    return render_template('student/index.html')

@app.route("/student/page2")
def student_page2():
    return render_template('student/page2.html')

if __name__ == '__main__':
    app.run(debug=True)