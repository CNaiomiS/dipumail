# Settings

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'c.naiomi.soto@gmail.com'
SMTP_PASSWORD = 'Naiomi393'
SMTP_FROM = 'c.naiomi.soto@gmail.com'
#SMTP_TO = 'meisameew@gmail.com'
#TEXT_FILENAME = '/Users/csotoba/documents/clau_cosas_random/test.txt'

# Now construct the message
import smtplib, email
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os

mailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
mailer.connect(SMTP_SERVER, SMTP_PORT)
mailer.ehlo()
mailer.starttls()
mailer.ehlo()
# EDIT: mailer is already connected
# mailer.connect()
mailer.login(SMTP_USERNAME, SMTP_PASSWORD)

fp = open('diputados.txt', encoding="ISO-8859-1")	
fd = open('test.txt')
text =  fd.read()
for line in fp.readlines():
	info = line.split(';');
	last_name = info[0].split(' ')[0]
	SMTP_TO = info[1]
	sexo = info[2]

	if sexo == 'M':
		est = 'Estimado Diputado'
	else:
		est = 'Estimada Diputada'


	intro = est + ' ' + last_name

	MESSAGE = intro +'\n\n'+ text

	msg = email.mime.multipart.MIMEMultipart()
	body = email.mime.text.MIMEText(MESSAGE)



	msg.attach(body)

	msg['Subject'] = 'Votación en sala sobre paridad de género, escaños reservados para pueblos originarios y listas de independientes para Convención Constituyente.'
	msg.add_header('From', SMTP_FROM)
	msg.add_header('To', SMTP_TO)

	# Now send the message

	mailer.sendmail(SMTP_FROM, [SMTP_TO], msg.as_string())
mailer.close()
