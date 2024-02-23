#5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key of your choice

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['user_input'] = user_input
        return redirect(url_for('index'))

    user_input = session.get('user_input', None)
    return render_template('index.html', user_input=user_input)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_input', None)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(host="0.0.0.0")












