from flask import Flask,request,render_template
app=Flask(__name__)

@app.errorhandler(404)
def page_not_found():
    return render_template('html.404'),404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'),500

@app.route('/')
def homepage():
    return "Welcome to home page"
@app.route('/not_found')
def not_found():
    return render_template('non_existent_template.html')

@app.route('/internal_server_error')
def internal_server_error_route():
    raise Exception('This is a simulated internal server error.')

if __name__ =='__main__':
    app.run(host='0.0.0.0')
                           