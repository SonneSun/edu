from flask import render_template, redirect, url_for, flash, jsonify, request, make_response
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required
from datetime import datetime
import json
import os


from . import main
from .. import db






class Mentor_profile(db.Model):
	__tablename__ = 'questions_dp'
	id = db.Column(db.Integer, primary_key = True)
	last_name = db.Column(db.Text)
	first_name = db.Column(db.Text)
	rating = db.Column(db.Integer)
	domain = db.Column(db.Text)
	introduction = db.Column(db.Text)
	pic_path = db.Column(db.Text)


class User_profile(db.Model):
	__tablename__ = 'questions_nlp'
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

	return render_template('homework_mentor.html')


@main.route('/booking_mask', methods=['GET','POST'])
def booking_mask():

	return render_template('booking_mask.html')
