from flask import escape, request, Flask, url_for,  redirect, render_template, session
from app import app
import twitter, json


def checkIfLogin():
	login = False
	if 'username' in session:
		# return 'Logged in as %s' % escape(session['username'])
		return True
	else:	
		return redirect(url_for('login'))
		return False
	# return login


@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():

	if checkIfLogin():
		return redirect(url_for('home'))
	if request.method == 'POST':
		session['username'] = request.form['username']
		redirect(url_for('home'))
		return '22'
	
	return render_template('login.html')
	# return '''
	# <form action="" method="post">
	# <p><input type=text name=username>
	# <p><input type=submit value=Login>
	# </form>
	# '''	
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

	return 'Login!'


@app.errorhandler(404)
def page_not_found(error):
	return redirect(url_for('login'))
	return render_template('404.html'), 404

@app.route('/home')
def home():
	if( checkIfLogin()):
		return 'this is home'
	else:
		return redirect(url_for('login'))