<<<<<<< HEAD
from flask import Flask,render_template,request,session,url_for,redirect
from flask_session import Session
from firebase_authenticate import *

app = Flask(__name__)
app.debug = True

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
@app.route('/onlinedocviewer',methods=['GET',"POST"])
def start():
	if request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password1')
		message = create_user(email,password) 
		if(message):
			return render_template('user_page.html',message = "error during registration: "+message)
	return render_template("register.html")

@app.route('/onlinedocviewer/login/document_view',methods=['POST'])
def document_page():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password1')
		result  = sign_in(email,password)
		if(result == True):
			return render_template('user_page.html')
		else:
			return redirect(url_for('invalid_login'))

@app.route('//onlinedocviewer/login/document_view/invalid_login')
def invalid_login():
	return render_template('invalid_login.html',message = "INVALID LOGIN CREDENTIALS OR MAYBE DETAILS NOT VERIFIED...CHECK THE MAIL SENT TO YOUR EMAIL ADDRESS.")

@app.route('/onlinedocviewer/login_page',methods = ['GET','POST'])
def login_page():
	return render_template('login.html')

if __name__=="__main__":
	app.run()

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("invalid_login.html"),message = "error 404")


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("invalid_login.html"),message = "error bad_request 400" )


@app.errorhandler(500)
def server_error():
    """Internal server error."""
=======
from flask import Flask,render_template,request,session,url_for,redirect
from flask_session import Session
from firebase_authenticate import *

app = Flask(__name__)
app.debug = True

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
@app.route('/onlinedocviewer',methods=['GET',"POST"])
def start():
	if request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password1')
		message = create_user(email,password) 
		if(message):
			return render_template('user_page.html',message = "error during registration: "+message)
	return render_template("register.html")

@app.route('/onlinedocviewer/login/document_view',methods=['POST'])
def document_page():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password1')
		result  = sign_in(email,password)
		if(result == True):
			return render_template('user_page.html')
		else:
			return redirect(url_for('invalid_login'))

@app.route('//onlinedocviewer/login/document_view/invalid_login')
def invalid_login():
	return render_template('invalid_login.html',message = "INVALID LOGIN CREDENTIALS OR MAYBE DETAILS NOT VERIFIED...CHECK THE MAIL SENT TO YOUR EMAIL ADDRESS.")

@app.route('/onlinedocviewer/login_page',methods = ['GET','POST'])
def login_page():
	return render_template('login.html')

if __name__=="__main__":
	app.run()

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("invalid_login.html"),message = "error 404")


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("invalid_login.html"),message = "error bad_request 400" )


@app.errorhandler(500)
def server_error():
    """Internal server error."""
>>>>>>> cf92c49ed7cb6ef17fffcb4de8ac8beb8d7ea70d
    return make_response(render_template("500.html"), 500)