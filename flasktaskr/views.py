# let's add some code :)
# Flask Task by - Catrell Washington, Last updated 7/1/2016
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, g
from functools import wraps
from forms import AddTaskForm, RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.exc import IntegrityError

#config

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#We're importing the file models
from models import Task, User

#Connecting to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE_PATH'])

#This function tells the user that you must be logged in to get to a private section.
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

#Logouts the user and takes them back to the main page.
@app.route('/logout/')
def logout():
	session.pop('logged_in', None)
	session.pop('user_id', None)
	flash("You have been logged out!")
	return redirect(url_for('login'))

#Logins in the user and takes them to the 'tasks' url.
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('Welcome!')
                return redirect(url_for('tasks'))
            else:
                error = 'Invalid username or password.'
        else:
            error = 'Both fields are required.'
    return render_template('login.html', form=form, error=error)

#Register routes to the register page
@app.route('/register/', methods =['GET','POST'])
def register():
	error=None
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_user = User(
				form.name.data,
				form.email.data,
				form.password.data,
			)
			try:
				db.session.add(new_user)
				db.session.commit()
				flash("Thanks for registering. Please login!")
				return redirect(url_for('login'))
			except IntegrityError:
				error="That username and/or email already exist."
				return render_template('registration.html', form=form, error=error)
	return render_template('registration.html', form=form, error=error)

#Defines open tasks with a status of 1
def open_tasks():
	return db.session.query(Task).filter_by(status='1').order_by(Task.due_date.asc())

#Defines closed tasks with a status of 0
def closed_tasks():
	return db.session.query(Task).filter_by(status='0').order_by(Task.due_date.asc())

#Making a tasks command section
@app.route('/tasks/')
@login_required
def tasks():
	return render_template(
		'tasks.html', 
		form=AddTaskForm(request.form),
		open_tasks=open_tasks(),
		closed_tasks=closed_tasks()
		)

#Add new tasks for the selected user 
@app.route('/add/', methods=['GET', 'POST'])
@login_required
def new_task():
	error = None
	form = AddTaskForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_task = Task(
				form.name.data,
				form.due_date.data,
				form.priority.data,
				'1',
				session['user_id'],
				datetime.datetime.utcnow()
			)
			db.session.add(new_task)
			db.session.commit()
			flash('New entry was successfully posted. Thanks!')
			return redirect(url_for('tasks'))
		else: 
			flash("Please put all credentials Necessary")
			return redirect(url_for('tasks'))
	return render_template('tasks.html', form=form, error=error, 
		open_tasks=open_tasks(), closed_tasks=closed_tasks())

#Mark tasks as completed
@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
	new_id= task_id
	db.session.query(Task).filter_by(task_id=new_id).update({"status":"0"})
	db.session.commit()
	flash('The task was marked as complete')
	return redirect(url_for('tasks'))

#Displays errors from forms.py
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error),'error')

#Delete tasks 
@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
	new_id = task_id
	db.session.query(Task).filter_by(task_id=new_id).delete()
	db.session.commit()
	flash('The task was deleted')
	return redirect(url_for('tasks'))