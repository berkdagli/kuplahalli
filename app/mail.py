from flask_mail import Mail
from flask_mail import Message

class E_Mail(Mail):
	
	def __init__(self,app):
		super().__init__(app)

	def sendMail(self,message):
		msg=Message('test',sender='kuplavalvonta@lohjanpallo.fi',recipients=['berkdagli1996@gmail.com','berkdagli@hotmail.com'])
		msg.body=message
		self.send(msg)
		
