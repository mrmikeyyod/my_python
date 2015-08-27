#!/usr/bin/python
from subprocess import call

print """ 
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       $       mikeys github project          $
       $     fill in the questions.           $
       $      add,commit,push or remove       $
       $     from your repo,  origin/master   $
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       

         would you like to add
         or remove a file?
          
         1) Add
         2) Remove"""
choice = raw_input(">    ")

if choice =="1":
 nf = raw_input("wich file you to add? >  ")
 raw_input("press enter to add file:..... "),
 call(["git", "add", nf])
 raw_input("press enter to commit.....")
 call(["git", "commit", "-m", nf])
 print "commited!!!!!"
 raw_input("press enter for git status: ")
 call(["git", "status"])
 raw_input("press enter to push to origin/master....")
 call(["git", "push", "origin", "master"])

if choice =="2":
 f4r = raw_input("wich file or dir? >")
 call(["git", "rm", "-r", f4r])
 raw_input("press enter to commit removal:")
 call(["git", "commit", "-m", f4r])
 raw_input("press enter to push:")
 call(["git", "push", "origin", "master"])
