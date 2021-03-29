#!/usr/bin/python3
'''nklineg || nklineg@gmail.com 
Best practce script and learning about input function'''

# constant / global (execution does not change)
ASTROS = "http://api.open-notify.org/astros.json"

def main():

    # input() is a standard library function
    urianswer = input("What is the URI you would like to look up:")
    print(urianswer)

def zfunc():
    return "yoyo"


main()
x = zfunc()
print(x)
