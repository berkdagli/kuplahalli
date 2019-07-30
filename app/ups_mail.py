from email.headerregistry import Address
from email.message import EmailMessage
import os
import smtplib
import sys

# Gmail details
email_address = "kuplavalvonta@lohjanpallo.fi"
email_password = "Lub12454"

# Recipent
to_address = (
	Address(username='berkdagli', domain='hotmail.com'),
	Address(username='kuplakopla', domain='lohjanpallo.fi')
)


def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

if sys.argv[1] == '0':
	title='Sähkökatko on ohi'
	text='Sähkökatko ohi kuplahallissa!'
else:
	title='Sähkökatko'
	text='Sähkökatko kuplahallissa!'

msg = create_email_message(
	from_address=email_address,
	to_address=to_address,
	subject=title,
	body=text,
)

smtp_server=smtplib.SMTP('smtp.office365.com', port=587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login(email_address, email_password)
smtp_server.send_message(msg)
