#!/usr/bin/python
from subprocess import call

nf = raw_input("which file to add?:")
raw_input("press enter to commit")
call(["git", "add", nf])
print """" press enter to commit:  >  """
call(["git", "commit", "-m", nf ])

print """
      Do you want to git push or see status?
      1) git status
      2) git push"""
option = raw_input("choose one:  ")

if option =="1":
 call(["git", "status"])
 raw_input("press enter to push ")
 call(["git", "push", "origin", "master"])

if option =="2":
 call(["git", "push", "origin", "master"])
