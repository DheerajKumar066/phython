# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
import re
import os
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

x = datetime.datetime.now()

fromaddr = "dheerajspan@gmail.com"


toaddr=["dheeraj979216@gmail.com","pradeep.shinde.11111@gmail.com","dheeraj979216@hotmail.com","dheeraj82990@gmail.com"]


# instance of MIMEMultipart
print("Length of sender "+str(len(toaddr))+".\n")

for i in range (0,len(toaddr)):
	msg = MIMEMultipart()

# storing the senders email address
	msg['From'] = fromaddr

	attached_file_name = {"dheeraj979216@gmail.com":"dheeraj.pdf","pradeep.shinde.11111@gmail.com":"pradeep.pdf","dheeraj979216@hotmail.com":"ganesh.pdf","dheeraj82990@gmail.com":"dhk.pdf"}
	# storing the receivers email address
	senderMailID = toaddr[i]
	print("Receivers mail id "+toaddr[i]+" .")
	print("File name "+attached_file_name[senderMailID]+" .")
    #attached_file_pattern = toaddr[i]

	# storing the subject
	msg['Subject'] = "Salary Slip"#"Subject of the Mail"

	# string to store the body of the mail
	body = """\
	<html>
	  <head>
	  </head>
	  <body>
	     <div style="background-color:#031857; color:#edeff5; text-align:center; margin-top: 25px;>
	  	</br>
	  	</br>
	  	</br>
	    <h1>Congratulation Your salary is credited</h1>
	    </br>
	    </br>
	    <h2>Please find the attachement</h2>
	    <h4>Note: use your birthdate and months as password</h4>
	    </br>
	    </br>
	    </br>
	    <br>
	    <h2>Thanks and Regards</h2>
	    <h3>HR Department</h3>
	    <h3>Span Pumps Pvt Ltd</h3>
	    <h3>Tower-2 office no-1001</h3>
	    <h3>Montreal Business Center</h3>
	    </div>
	  </body>
	</html>
	"""
	# body = "Hello,\n\nSalary slip for the month of "+x.strftime("%b %Y")+".\n\nPassword : Use your birthday date and month.\nFor example 10.05.1999 then it will be 1005.\n\nThanks & Regards,\nHR Department\nSpan Pumps"#"Body_of_the_mail"

	# attach the body with the msg instance
	# msg.attachMIMEText(html,'html')
	html = MIMEText(body, 'html')
	msg.attach(html)
	# open the file to be sent
	#filename.clear();#check with it also and without it
	filename = attached_file_name[senderMailID]#"Span Pumps.xlsx"#"File_name_with_extension"
	attachment = open("/home/linux/DHK/Span/MailSent/Encrypted_PDF-Files/"+filename,"rb")#open("Path of the file", "rb")

	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')

	# To change the payload into encoded form
	p.set_payload((attachment).read())

	# encode into base64
	encoders.encode_base64(p)

	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	# attach the instance 'p' to instance 'msg'
	msg.attach(p)

	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	#s = smtplib.SMTP('smtp.office365.com', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	#s.login(fromaddr, "PASSWORD")		#******** - put password here
	s.login(fromaddr, "Spanpumps123@")

	# Converts the Multipart msg into a string
	text = msg.as_string()

	# sending the mail
	s.sendmail(fromaddr, senderMailID, text)

	# terminating the session
	#os.remove("/home/spaneye/Downloads/"+attached_file_name[senderMailID])
	#shutil.copyfile("/home/spaneye/Downloads/"+attached_file_name[senderMailID], "/home/spaneye/python/")
	s.quit()

	#print("Text variable "+text)
	#print("P "+str(p))
	"""\
	<html>
	  <head>
	  </head>
	  <body>
	     <div style="background-color:#031857; color:#edeff5; text-align:center"  margin-top: 25px;>
	  	</br>
	  	</br>
	  	</br>
	    <h1>Congratulation Your salary is credited</h1>
	    </br>
	    </br>
	    <h2>Please find the attachement</h2>
	    <h4>Note: use your birthdate and months as password</h4>
	    </br>
	    </br>
	    </br>
	    <br>
	    <h2>Thanks and Regards</h2>
	    <h3>HR Department</h3>
	    <h3>Span Pumps Pvt Ltd</h3>
	    <h3>Tower-2 office no-1001</h3>
	    <h3>Montreal Business Center</h3>
	    </div>
	  </body>
	</html>
	"""

	senderMailID = ""
	filename = ""
	#attachment = ""
	p = ""
	attached_file_name = ""
	body = ""
	# if (attachment is None):
	# 	print("Attachment is already null")
	# else:
	# 	print("Attachment is not null")
	# 	attachment = open("/home/linux/DHK/Span/MailSent/Encrypted_PDF-Files/","rb")
	# 	p = MIMEBase('application', 'octet-stream')
	# 	p.set_payload((attachment).read())
	#filename.clear();
	#print("Text variable "+text)
	#print("P "+str(p))
