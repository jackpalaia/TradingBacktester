import pandas as pd
import csv
import json

def getDixData():
    """ Gets DIX index data from DIX.csv, dates are start and end date in settings.json """
    with open('settings.json', 'r') as settings:
        data = json.load(settings)