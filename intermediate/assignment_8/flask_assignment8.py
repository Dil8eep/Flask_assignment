#8. Implement user authentication and registration in a Flask app using Flask-Login.
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'Prasad_reddy'
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

# Replace this dictionary with a database in a real application
users = {
    'user1': {'id': "prasad1", 'password': 'password1'},
    'user2': {'id': "prasad2", 'password': 'password2'}
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route("/", methods=["GET", "POST"])
def login_or_register():
    if request.method == "POST":
        action = request.form.get("action")
        user_name = request.form.get("name")
        password = request.form.get("password")

        if action == "login":
            user = users.get(user_name)
            if user and password == user['password']:
                login_user(User(user['id'], user_name, password))
                flash(f"Login successful for {user_name}", 'success')
            else:
                flash("Invalid credentials. Please try again.", 'danger')
        elif action == "register":
            if user_name and password:
                # Replace this with actual user registration logic, e.g., adding to a database
                new_user = User(len(users) + 1, user_name, password)
                users[user_name] = {'id': new_user.id, 'password': password}
                flash(f"Registration successful for {user_name}", 'success')

    return render_template("login_register.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout successful.", 'success')
    return redirect(url_for("login_or_register"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
