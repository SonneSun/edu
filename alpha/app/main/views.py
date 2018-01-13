from flask import render_template, redirect, url_for, flash, jsonify, request, make_response
from flask_wtf import FlaskForm
from wtforms import TextField
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


class QuestionForm(FlaskForm):
	body = TextField("",validators=[Required()])




#The home page
@main.route('/', methods=['GET','POST'])
def index():

	return render_template('index.html')


#The home page, default is analytics
@main.route('/homework_mentor', methods=['GET','POST'])
def homework_mentor():
	mentors = MentorProfile.query.all()

	return render_template('homework_mentor.html', mentors = mentors)


@main.route('/booking_mentor/<mentor_full_name>', methods=['GET','POST'])
def booking_mentor(mentor_full_name):

	return render_template('booking_mentor.html', mentor_full_name = mentor_full_name)
