#!/usr/bin/python3

import requests

# define API were are going to interact with
ISSNOW = 'http://api.open-notify.org/iss-now.json'

def main() :
    # mage request to that API (send HTTP GET)
    r = requests.get(ISSNOW)
    
    # capture 200 response (we expect JSON on this)
    # strip JSON off 200 response and write into a file
    with open("iss_location", "a") as issloc:
        issloc.write("The current location of the ISS is:\n")
        issloc.write(str(r.json()) + "\n")

if __name__ == "__main__":
    main()
