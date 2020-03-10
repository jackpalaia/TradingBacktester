import pandas as pd
import csv
import json
import datetime as dt
from GetData import generateNDayForwardReturn

def getDixData():
    """ Gets DIX index data from DIX.csv, dates are start and end date in settings.json """
    with open('settings.json', 'r') as settings:
        data = json.load(settings)

    tickers = data['tickers']

    # startData, endDate are dates in datetime format
    start = tuple([int(i) for i in data['start'].split(',')])
    end = tuple([int(i) for i in data['end'].split(',')])
    startDate = dt.datetime(start[2], start[0], start[1])
    endDate = dt.datetime(end[2], end[0], end[1])

    # startDateString, endDateString are lists containing strings of year, month, data
    startDateString = list([str(i) for i in start])
    endDateString = list([str(i) for i in end])

    # create dataframe containing indicator values from DIX.csv
    DIXData = pd.DataFrame(columns=data['tickers'], index=start)
    DIXData.iloc[0].index = startDate
    print(DIXData)

    with open('DIX.csv', 'r') as dix:
        reader = csv.reader(dix)
        next(reader)
        for row in reader:
            if (row[0] == '{0}/{1}/{2}'.format(startDateString[0], startDateString[1], startDateString[2])):
                while True:
                    dateTuple = tuple([int(i) for i in row[0].split('/')])
                    date = dt.datetime(dateTuple[2], dateTuple[1], dateTuple[0])
                    DIXData.iloc[1] = row[2]
                    if (row[0] == '{1}/{2}/{0}'.format(endDateString[0], endDateString[1], endDateString[2])):
                        break

    print(DIXData)

getDixData()