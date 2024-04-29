import requests

# Login test (Sucessful login)
def test_login():
    data = {'email': 'test@example.com', 'password': 'password'}
    response = requests.post('http://localhost:5000/login', json=data)
    assert response.status_code == 200
    assert response.json().get('message') == 'Login successful'

# Login test (Invalid credentials)
def test_login_invalid_credentials():
    data = {'email': 'invalid@example.com', 'password': 'wrongpassword'}
    response = requests.post('http://localhost:5000/login', json=data)
    assert response.status_code == 401
    assert response.json().get('error') == 'Invalid email or password'

# Signup test (Sucessful signup)
def test_signup():
    data = {'name': 'New User', 'email': 'new@example.com', 'password': 'password123', 'confirm_password': 'password123'}
    response = requests.post('http://localhost:5000/signup', json=data)
    assert response.status_code == 201
    assert response.json().get('message') == 'Signup successful'
    assert 'id' in response.json().get('user')
    assert response.json().get('user').get('name') == 'New User'
    assert response.json().get('user').get('email') == 'new@example.com'

# Signup test (Passwords don't match)
def test_signup_mismatched_passwords():
    data = {'name': 'Test User', 'email': 'new2@example.com', 'password': 'password', 'confirm_password': 'differentpassword'}
    response = requests.post('http://localhost:5000/signup', json=data)
    assert response.status_code == 400
    assert response.json().get('error') == 'Passwords do not match'

print("Running tests...")
print("Test 1: Login (Sucessful login):", end=' ')
try:
    test_login()
    print("Passed")
except:
    print("Failed")

print("Test 2: Login (Invalid credentials):", end=' ')
try:
    test_login_invalid_credentials()
    print("Passed")
except:
    print("Failed")

print("Test 3: Signup (Sucessful signup):", end=' ')
try:
    test_signup()
    print("Passed")
except:
    print("Failed")

print("Test 4: Signup (Passwords don't match):", end=' ')
try:
    test_signup_mismatched_passwords()
    print("Passed")
except:
    print("Failed")

print("All tests over!")