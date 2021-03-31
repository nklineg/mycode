#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

num_lines = sum(1 for line in open('vlanconfig.cfg'))

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("\nTotal line count = " + str(num_lines))
