#!/usr/bin/env python3
"""Requests for Flask App Project
-GET request sent to Flask API
-use pprint to display json response"""

## import request and pprint module
import requests
from pprint import pprint

def main():

    # endpoint url
    allordersurl= "http://127.0.0.1:2224/allorders"

    # get data from the server and turn into json
    resp= requests.get(allordersurl).json()

    # print to console
    pprint(resp)

# run main
if __name__ == "__main__":
    main()