import pyrebase
import requests.exceptions
import json

Config = {
  "apiKey": "AIzaSyAhyjAPeD33Tg3Ik9_YGVg4wgiuL_Q6nHU",
  "authDomain": "onlinedocviewer.firebaseapp.com",
  "databaseURL": "https://onlinedocviewer.firebaseio.com",
  "projectId": "onlinedocviewer",
  "storageBucket": "onlinedocviewer.appspot.com",
  "messagingSenderId": "1016559152547",
  "appId": "1:1016559152547:web:5bd92b5cbf04882575fe16",
  "measurementId": "G-49XHC1HDPR"
};

firebase = pyrebase.initialize_app(Config)
# email = input("ENTER AN EMAIL: ")
# password = input("ENTER A PASSWORD:")

def create_user(email,password):
	try:
		auth = firebase.auth()
		db = firebase.database()
		user = auth.create_user_with_email_and_password(email,password)
		auth.send_email_verification(user['idToken'])
		data = {"active":'N'}
		db.child('users').set(email)
		db.child('users').child(email).update(data)

	except requests.exceptions.HTTPError as httpErr:
		error_message = json.loads(httpErr.args[1])['error']['message']
		return error_message

def sign_in(email,password):
	try:
		auth = firebase.auth()
		user = auth.sign_in_with_email_and_password(email,password)
		token = auth.get_account_info(user['idToken'])
		if token['users'][0]['emailVerified'] == False:
			return False
		if(token):
			return True
	except requests.exceptions.HTTPError as httpErr:
		error_message = json.loads(httpErr.args[1])['error']['message']
		print(error_message)

def update(email):
	db = firebase.database()
	# data = {"active":'Y',"email":email}
	# db.child('users').push(data)
	# db.child('users').child(email)
	
def main():
	update('me.manu101@gmail.com')
if __name__ == '__main__':
	main()

