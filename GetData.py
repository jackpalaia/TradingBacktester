import pandas as pd
import pandas_datareader as web
import datetime as dt
import json

def generatePriceDF():
    # getting start and end dates as well as stock tickers from settings.json
    with open('settings.json', 'r') as settings:
        data = json.load(settings);
    start = tuple([int(i) for i in data['start'].split(',')])
    end = tuple([int(i) for i in data['end'].split(',')])
    tickers = data['tickers']
    startDate = dt.datetime(start[0], start[1], start[2])
    endDate = dt.datetime(end[0], end[1], end[2])
    
    priceDF = pd.DataFrame()
    dfList = []
    for ticker in tickers:
        tempdf = pd.DataFrame()
        df = web.DataReader(ticker, 'yahoo', startDate, endDate)
        tempdf[ticker] = round(df['Close'], 2)
        dfList.append(tempdf)
    priceDF = pd.concat(dfList, axis=1, sort=False)

    print(priceDF)
    return priceDF

generatePriceDF()