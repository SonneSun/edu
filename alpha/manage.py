#!/usr/bin/python

import os
from app import create_app, db

app, db = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
	app.run()
