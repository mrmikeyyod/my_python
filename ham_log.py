#! /usr/bin/python
#my first simple ham radio contact logger
#very first pyhon program
#please be gentle
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
raw_input( )
print """

"""

#lets start
print "hit cntrl+c to exit"
raw_input(" press enter if you don't want to exit.")
print """


"""

print """ enter the name of your log file including .txt
if you dont have one just enter the name you want your log file to be"""

""" 

"""
#File name
file = raw_input("> ")
print """


"""

#open file
file_open = open(file, 'a')

print "lets start logging!!!!"
raw_input("press enter ")
print """

 just follow the prompt. enter callsign,name,date. ahd thats it.
it will ask a question. pressing n will end the loop. close and save your log."""
print"""

"""
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
 file_open.write(callsign)
 file_open.write(" ")
 file_open.write(name)
 file_open.write(" ")
 file_open.write(freq)
 file_open.write(" ")
 file_open.write(quality)
 file_open.write(" ")
 file_open.write(date)
 file_open.write( " ")
 file_open.write(comment)
 file_open.write(" ")
 file_open.write("\n")
 Q = raw_input("Add another log? Y/N? ")
 print " "
 print " "
 print " "
 if Q == "n":
  file_open.close()
  break

#file should be closed and sved. 
print """
Thanks for using this program. this is my first program. any feedback
would be fantastic!!!!   
email comments or suggestions to me at
mrmikeyyod@gmail.com
73'3 to all"""
#exit