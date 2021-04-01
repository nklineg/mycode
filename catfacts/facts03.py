#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    
    i = 0
    f = []
    
    for catfact in r.json():
        #print(catfact.get("text"))
        f.append(catfact.get("text"))

    cprint(figlet_format('Random Cat Factoid!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])

    print(random.choice(f) + "\n")

main()

