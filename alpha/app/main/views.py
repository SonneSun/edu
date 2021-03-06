from flask import render_template, redirect, url_for, flash, jsonify, request, make_response
from wtforms import Form, TextField, validators, SubmitField
from wtforms.validators import Required
from datetime import datetime
import json
import os


from . import main
from .. import db



class MentorProfile(db.Model):
	__tablename__ = 'mentor_profile'
	id = db.Column(db.Integer, primary_key = True)
	last_name = db.Column(db.Text)
	first_name = db.Column(db.Text)
	full_name = db.Column(db.Text)
	rating = db.Column(db.Integer)
	domain = db.Column(db.Text)
	introduction = db.Column(db.Text)
	pic_path = db.Column(db.Text)


class UserProfile(db.Model):
	__tablename__ = 'user_profile'
	id = db.Column(db.Integer, primary_key = True)
	last_name = db.Column(db.Text)
	first_name = db.Column(db.Text)
	email = db.Column(db.Text)

class MentorDetail(db.Model):
    __tablename__ = 'mentor_detail'
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.Text)
    topic_detail = db.Column(db.Text)
    time_detail = db.Column(db.Text)


class MyForm(Form):
    date = SubmitField()



#The home page
@main.route('/', methods=['GET','POST'])
def index():

	return render_template('index.html')


#The home page, default is analytics
@main.route('/homework_mentor', methods=['GET','POST'])
def homework_mentor():
	mentors = MentorProfile.query.all()

	return render_template('homework_mentor.html', mentors = mentors)


@main.route('/booking_mentor/<param>', methods=['GET','POST'])
def booking_mentor(param):
	form = MyForm(request.form)

	if request.method == 'POST':
		post_id = request.form.get('day')
		if post_id is not None:
			print post_id
		return render_template('booking_mentor.html', param = param, form=form)


	elif request.method == 'GET':
		return render_template('booking_mentor.html', param = param, form=form)
