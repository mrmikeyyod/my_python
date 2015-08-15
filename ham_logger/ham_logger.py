#!/usr/bin/python
print """
-------------------------------------------------
|                                                |
|   WELCOME TO MIKEYS HAM-RADIO CONTACT LOGGER   |  
|                                                |
|IF YOU HAVE ANY SUGGESTIONS.........            |
|           SEND TO mrmikeyyod@gmail.com         |
|   THANKS AND HAVE A GOOD TIME LOGGING....      |
|               73's to all                      |
|________________________________________________|

Press Enter Key to Continue:......."""
raw_input() 
print """ enter the name of your log file including .txt
if you dont have one just enter the name you want your log file to be"""
print '\n\n'
file = raw_input("> ")
print '\n\n\n'
opnf = open(file, 'a')
print "lets start logging!!!!"
raw_input("press enter ")
print """
just follow the prompt. enter callsign,name,date. ahd thats it.
it will ask a question. pressing n will end the loop. close and save your log."""
print '\n\n\n'
#begin input loop here
var = 1
while var ==1 :
 print "NEW LOG"
 print " " 
 callsign = raw_input("enter callsign: ")
 name = raw_input("enter name: ")
 freq = raw_input("enter frequency: ")
 quality = raw_input("enter quality: ")
 date = raw_input("enter date: ")
 comment = raw_input("enter comments if none, just press enter: ")
 opnf.write(callsign+ "\n"+ name+"\n"+ freq+"\n"+ quality+"\n"+ date+"\n"+ comment+"\n")
 Q = raw_input("Add another log? Y/N? ")
 print "\n\n\n"
 if Q == "n":
  opnf.close()
  break
print """
Thanks for using this program. this is my first program. any feedback
would be fantastic!!!!   
email comments or suggestions to me at
mrmikeyyod@gmail.com
73'3 to all"""