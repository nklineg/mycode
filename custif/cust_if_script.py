#!/usr/bin/env python3

message = 'You are experiencing a hurricane category '

windspeed = float(input("What wind speed are you encountering?"))

if windspeed >= 157:
    message = message + 'FIVE! Hold on Dorothy, Kansas is going bye-bye!'
elif windspeed >= 130:
    message = message + "FOUR: Hunker down, it's gonna get rough."
elif windspeed >= 111:
    message = message + 'THREE. Did someone say hurricane party?'
elif windspeed >= 96:
    message = message + 'TWO. Just a sligh breeze.'
elif windspeed >= 74:
    message = message + 'ONE. Perfect time to fly a kite!'
else:
    message = "No hurricane present. It's a beautiful day in the neighborhood."


print(message)

