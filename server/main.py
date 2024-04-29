from flask import Flask, request, jsonify, render_template, abort
import bcrypt
import uuid

app = Flask(__name__)

# Sample user database
users = [{
        'id': str(uuid.uuid4()),
        'name': 'Test User',
        'email': 'test@example.com',
        'password': '$2b$12$vTTgl50tjnztWcPqQzt5Ve4TGsnYYII/wNrC2y2Iu2E9WZj.Hwuk2'
    }]

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

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
    
    email = request.json.get('email')
    password = request.json.get('password')

    abort(500)

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    repassword = request.json.get('repassword')
    teacher_or_student = request.json.get('selectedtoggle')

    abort(500)

if __name__ == '__main__':
    app.run(debug=True)