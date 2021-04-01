#!/usr/bin/python3

'''Norm Kline's Dad Joke Generator from API
   April 1, 2021
'''

import requests
import json
import crayons

# set API URI
APOD = 'https://dad-jokes.p.rapidapi.com/random/joke'

# set API call to get a random joke
def getjoke():
    jokeheader = {'x-rapidapi-key': "d6961b6a0bmsh6200445b9bb8a0dp192b7cjsnaf3536237750",'x-rapidapi-host': "dad-jokes.p.rapidapi.com"}
    
    # load request
    r = requests.request("GET", APOD, headers = jokeheader)
    
    # set request data to json
    data = r.json()
    
    # set json 
    json_str = json.dumps(data)
    
    # json decode
    resp = json.loads(json_str)
    
    # set variables
    j = resp['body'][0]['setup']
    pl = resp['body'][0]['punchline']
    
    # asseble joke and punchline string
    joke = "\n\n" + crayons.red(str(j), bold=True) + "\n\n" + crayons.green(str(pl), bold=True) + "\n\n"
    
    return joke


def main():

    #set counter
    drnd = 0

    # print name of the same on the screen
    print("\n**************************Random Dad Jokes***************************\n\n") 

    while True:        # sets up an infinite loop condition
        
        if drnd == 0:
            answer = input("Do you want to hear a dad joke? (Y/N) ") # string ans collected from user
        else:
            answer = input("Do you want to hear ANOTHER dad joke? (Y/N) ")
        
        if answer.lower() == 'y': # logic to check if user gave correct answer
            print(getjoke())
        else:                 # if answer was wrong, and round is not yet equal to 3
            print(crayons.yellow("\n\nWell... Bye.\n\n"))
            break
        
        drnd = drnd + 1     # increase the round counter


if __name__ == "__main__":
    main()
