#!/usr/bin/env python3

#define list my_list
my_list = [ "192.168.0.5", 5060, "UP" ]

#print the IP address from my_list
print("The first item in the list (IP): " + my_list[0] )

#print the port number from my_list
print("The second item in the list (port): " + str(my_list[1]) )

#print the state from my_list
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("When I ssh into IP address ", new_list[3], " or ", new_list[4], " I am unable to pint ports ", str(new_list[0]), ", ",  new_list[1], ", or ", new_list[2], ".")
