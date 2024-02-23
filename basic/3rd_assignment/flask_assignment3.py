from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def display():
    return f"please enter name in the search bar with the syntax of '/user/Name'."

@app.route('/user/<name>')
def greet(name):
    return render_template('home.html', name=name)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)

