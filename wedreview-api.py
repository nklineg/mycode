#!/usr/bin/python3

# make HTTP requests
import requests

CATFACTS = 'https://cat-fact.herokuapp.com/facts'

def main():
    
    # make request call to URI
    r = requests.get(CATFACTS)

    #strip JSON off of response (r)
    catfacts = r.json()

    # open file to write to
    with open("cat.facts", "w") as cf:
        # loop through data
        for catfact in catfacts:
            #cf.write(catfact.get("text") + "\n")
            print(catfact.get("text"), file=cf, end="\n")
    
    # place the key "text" in our open file

if __name__ == "__main__":
    main()
