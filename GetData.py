import pandas as pd
import pandas_datareader as web
import datetime as dt
import json


def generatePriceDF():
    """ Pulls stock data from start date to end date from yahoo finance """
    # getting start and end dates as well as stock tickers from settings.json
    with open('settings.json', 'r') as settings:
        data = json.load(settings);
    start = tuple([int(i) for i in data['start'].split(',')])
    end = tuple([int(i) for i in data['end'].split(',')])
    tickers = data['tickers']
    startDate = dt.datetime(start[0], start[1], start[2])
    endDate = dt.datetime(end[0], end[1], end[2])
    
    # pulling data from yahoo finance, putting closing prices of each stock for each day in dataframe
    priceDF = pd.DataFrame()
    dfList = []
    for ticker in tickers:
        tempdf = pd.DataFrame()
        df = web.DataReader(ticker, 'yahoo', startDate, endDate)
        tempdf[ticker] = round(df['Close'], 2) # rounding prices to 2 decimal points
        dfList.append(tempdf)
    priceDF = pd.concat(dfList, axis=1, sort=False) # turning dataframe list into actual dataframe

    print(priceDF)
    return priceDF

def generateNDayForwardReturn():
    """ Uses generatePriceDF() to generate N day forward return for each stock on each day """


generatePriceDF()