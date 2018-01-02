from flask import render_template, redirect, url_for, flash, jsonify, request, make_response
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required
from datetime import datetime
import json
import os


from . import main
from .. import db






class Question_dp(db.Model):
	__tablename__ = 'questions_dp'
	id = db.Column(db.Integer, primary_key = True)
	question = db.Column(db.Text)
	intent = db.Column(db.Text)
	scope = db.Column(db.Text)

class Question_nlp(db.Model):
	__tablename__ = 'questions_nlp'
	id = db.Column(db.Integer, primary_key = True)
	question = db.Column(db.Text)
	sql = db.Column(db.Text)


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
