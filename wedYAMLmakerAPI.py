#!/usr/bin/python3

# import pyyaml
import yaml

# make HTTP requests
import requests

CATFACTS = 'https://cat-fact.herokuapp.com/facts'

def main():
    
    # make request call to URI
    r = requests.get(CATFACTS)

    #strip JSON off of response (r)
    catfacts = r.json()

    # open file to write to
    with open("cat.facts.yml", "w") as cf:
        print(yaml.dump(catfacts), file=cf)

if __name__ == "__main__":
    main()
