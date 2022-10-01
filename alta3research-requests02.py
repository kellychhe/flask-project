#!/usr/bin/env python3
"""Requests for Flask App Project
-GET request sent to Flask API
-use pprint to display json response"""

## import request, yaml and pprint module
import requests
import yaml
from pprint import pprint

def main():

    # endpoint url
    allordersurl= "http://127.0.0.1:2224/allorders"

    # get data from the server and turn into json
    resp= requests.get(allordersurl).json()

    # turn data to yaml for readability
    yamlresp = yaml.dump(resp, sort_keys=False, explicit_start=True, default_flow_style=False)

    # print to console
    pprint(yamlresp)

# run main
if __name__ == "__main__":
    main()