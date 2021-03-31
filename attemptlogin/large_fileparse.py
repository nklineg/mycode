#!/usr/bin/python3

# parse keystrone.common.wsgi and return number of failed login attempts
loginfail = 0

#open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

# look over the file
for line in keystone_file:

    # if this 'fail pattern' appears in the line...
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed login attempts is", loginfail)
keystone_file.close()
