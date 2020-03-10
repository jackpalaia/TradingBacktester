import pandas as pd
import pandas_datareader as web
import datetime as dt
import json

def generatePriceDF():
    """ Pulls stock data from start date to end date from yahoo finance """
    # getting start and end dates as well as stock tickers from settings.json
    with open('settings.json', 'r') as settings:
        data = json.load(settings)
    start = tuple([int(i) for i in data['start'].split(',')])
    end = tuple([int(i) for i in data['end'].split(',')])
    tickers = data['tickers']
    startDate = dt.datetime(start[2], start[0], start[1])
    endDate = dt.datetime(end[2], end[0], end[1])
    
    # pulling data from yahoo finance, putting closing prices of each stock for each day in dataframe
    priceDF = pd.DataFrame()
    dfList = []
    for ticker in tickers:
        tempdf = pd.DataFrame()
        df = web.DataReader(ticker, 'yahoo', startDate, endDate)
        tempdf[ticker] = round(df['Close'], 2) # rounding prices to 2 decimal points
        dfList.append(tempdf)
    priceDF = pd.concat(dfList, axis=1, sort=False) # turning dataframe list into actual dataframe

    return priceDF

def generateNDayForwardReturn():
    """ Uses generatePriceDF() to generate n day forward return for each stock on each day """
    # gets value of n from settings.json
    with open('settings.json', 'r') as settings:
        n = json.load(settings)['returnPeriod']
    
    pricesDF = generatePriceDF()
    # creates new dataframe with same rows and columns as prices dataframe
    returnsDF = pd.DataFrame(columns = pricesDF.columns, index = pricesDF.index[:-n])

    # loops through each cell of priceDF
    for i in range(len(pricesDF.index) - n):
        for ticker in pricesDF.columns:
            # n day forward return calculated as: (close of current day+n days - close of current day) / close of current day
            decimalReturn = (pricesDF.iloc[i + n].loc[ticker] - pricesDF.iloc[i].loc[ticker]) / pricesDF.iloc[i].loc[ticker]
            returnsDF.iloc[i].loc[ticker] = round((decimalReturn * 100), 3) # multiplies decimal return by 100 to get percent return, rounds to 3 decimal places
    
    return returnsDF

print(generateNDayForwardReturn())