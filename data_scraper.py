import pandas_datareader.data as web
import os
import datetime

def download_data(tickers,start='all',end='all',metric=False,all_data=False):
    if all_data==True:
        end = datetime.datetime.now
        end = '%s-%s-%s' % (end.month,end.day,end.year)
        start = '01-01-1970'

    directory = 'stock_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    d = {}
    for ticker in tickers:
        filename = directory+'/'+ticker+'.csv'
        d[ticker] = web.DataReader(ticker,"yahoo",start,end)
        d[ticker].to_csv(filename)
        return

if __name__ == '__main__':
    tickers = ['AAPL','BAC','GILD']
    start = '2016-01-01'
    end = '2016-12-21'
    end = 'today'
    metric='Adj Close' #this will give us open, high, low, close, volume, Adj Close
    download_data(tickers,start,end,metric)
