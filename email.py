import smtplib
s = smtplib.SMTP('localhost', 1025)
s.sendmail('zigmyalwangchuk@gmail.com','zigmyalwangchuk@hotmail.com', 'Python email')
