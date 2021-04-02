#!/usr/bin/python3

'''Norm Kline's Dad Joke Generator from API
   Alta3 Python Certification Attempt 
   April 2, 2021
'''

# get requests library
import requests

# get json library
import json

# get our colorful crayons 
import crayons


# set API URI
APOD = 'https://dad-jokes.p.rapidapi.com/random/joke'


# set api call, getting stored key
def makeapicall():

    # get our api key from a secure dir
    dj_api_keyfile = open("/home/student/dj.cred", "r")
    
    # set our local key value
    dj_api_key = dj_api_keyfile.read().rstrip('\n')

    # set header for api call with the stored key
    jokeheader = {'x-rapidapi-key': dj_api_key,'x-rapidapi-host': "dad-jokes.p.rapidapi.com"}
   
    # load request
    r = requests.request("GET", APOD, headers = jokeheader)

    # set our json 
    jokedata = r.json()

    return jokedata;        


# set API call to get a random joke
def getjoke():
    
    # call api and return our base data set
    jokedata = makeapicall()

    # set variables
    setup = jokedata['body'][0]['setup']
    punchline = jokedata['body'][0]['punchline']
    
    # asseble joke and punchline string
    joke = "\n\n" + crayons.red(str(setup), bold=True) + "\n\n" + crayons.green(str(punchline), bold=True) + "\n\n"
    
    return joke



# do the main thing... 
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
