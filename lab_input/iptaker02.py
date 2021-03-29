#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("you told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)

user_input2 = input("Please enter the vendor name of your device:")
print("Your device vendor:", user_input2)
