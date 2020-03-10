import pandas as pd
import csv
import json
import datetime as dt

def getDixData():
    """ Gets DIX index data from DIX.csv, dates are start and end date in settings.json """
    with open('settings.json', 'r') as settings:
        data = json.load(settings)

    tickers = data['tickers']

    # startData, endDate are dates in datetime format
    start = tuple([int(i) for i in data['start'].split(',')])
    end = tuple([int(i) for i in data['end'].split(',')])
    startDate = dt.datetime(start[0], start[1], start[2])
    endDate = dt.datetime(end[0], end[1], end[2])

    # startDateString, endDateString are lists containing strings of year, month, data
    startDateString = list([str(i) for i in start])
    endDateString = list([str(i) for i in end])

    # create dataframe containing indicator values from DIX.csv
    DIXData = pd.DataFrame(columns=data['tickers'])

    with open('DIX.csv', 'r') as dix:
        reader = csv.reader(dix)
        for row in reader:
            if (row[0] == '{1}/{2}/{0}'.format(startDateString[0], startDateString[1], startDateString[2])):
                DIXData.append(row[2])

    DIXData.append(['2'])
    print(DIXData)

getDixData()