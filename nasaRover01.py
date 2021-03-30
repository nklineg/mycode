#!/usr/bin/python3

import requests

API = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY'

def main():
    r = requests.get(API)

    # get data from 200 response
    nasadata = r.json()
    
    # loop across all the dictionaries within the list called 'photos'
    for pic in nasadata.get('photos'):
        # get list of URLs
       print(pic.get('img_src'))


main()
