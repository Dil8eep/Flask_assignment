from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        user_input = request.form['user_input']
        return render_template("home.html",user_input=user_input) 
    return render_template("home.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005)