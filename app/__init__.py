from flask import Flask
from app import database
from app import mail
import time
import sys

#Construct Web App
app=Flask(__name__)

from app import routes

#Configure mail settings
app.config['MAIL_SERVER']='smtp.office365.com'
app.config['MAIL_USERNAME']='kuplavalvonta@lohjanpallo.fi'
app.config['MAIL_PASSWORD']='Lub12454'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

email = mail.E_Mail(app)

'''
with app.app_context():
	email.sendMail("test message")
'''

