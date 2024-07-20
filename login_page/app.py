from flask import Flask, render_template, request, redirect, url_for, flash
from models import User

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database (can be replaced with SQLAlchemy or any other ORM)
users = []

# Mock function to check if username exists
def username_exists(username):
    return any(user.username == username for user in users)

# Route for registering a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        full_name = request.form.get('full_name', '')
        contact_info = request.form.get('contact_info', '')

        # Basic validation
        if not (username and email and password and confirm_password):
            flash('All fields are required.', 'error')
        elif password != confirm_password:
            flash('Passwords do not match.', 'error')
        elif username_exists(username):
            flash('Username already exists. Please choose a different username.', 'error')
        else:
            # Register the user (here we just add to mock database)
            new_user = User(username, email, password, full_name, contact_info)
            users.append(new_user)
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Mock authentication (replace with real authentication logic)
        authenticated = any(user.username == username and user.password == password for user in users)

        if authenticated:
            flash('Login successful.', 'success')
            return redirect("http://localhost:5173/")
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
