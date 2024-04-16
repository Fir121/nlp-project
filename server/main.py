from flask import Flask, request, jsonify
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

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email is None or password is None:
        return jsonify({"error": "Email and password are required"}), 400

    # Simulate user authentication (in a real application, check against a database)
    authenticated = False
    for user in users:
        if user['email'] == email and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            authenticated = True
            break

    if authenticated:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if name is None or email is None or password is None or confirm_password is None:
        return jsonify({"error": "All fields are required"}), 400
    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    # Check if email is already in use
    if any(user['email'] == email for user in users):
        return jsonify({"error": "Email already in use"}), 400

    # Hash the password
    hashed_password = hash_password(password)

    # Create a new user
    new_user = {
        'id': str(uuid.uuid4()),
        'name': name,
        'email': email,
        'password': str(hashed_password)
    }

    users.append(new_user)

    return jsonify({"message": "Signup successful", "user": new_user}), 201

if __name__ == '__main__':
    app.run(debug=True)