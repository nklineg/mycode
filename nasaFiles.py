#!/usr/bin/python3

import requests

APOD = 'https://api.nasa.gov/planetary/apod?api_key='


# open file and read out cred ~/nasa.cred
def nasacred():
    with open("/home/student/nasa.cred", "r") as f:
        nasakey = f.read()
        nasakey = nasakey.rstrip("\n")
        return nasakey

def main():
    
    # make API lookup to NASA APOD
    r = requests.get(APOD + nasacred())
   
    # determine if r is a "200"
    if r.status_code != 200:
        print(r.status_code)
        print(r.json())
        exit()

    #grab JSON off our response
    r = r.json()

    # open file to write out data (append mode)
    with open("apod.data", "a") as f:
        # write out title
        f.write(str(r.get("title")) + "\n")
        f.write(str(r.get("date")) + "\n")
        f.write(str(r.get("hdurl")) + "\n\n")

if __name__ == "__main__":
    main()
