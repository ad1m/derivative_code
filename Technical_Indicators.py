__author__ = 'Adamlieberman'
from Portfolio_Constructor import *
import matplotlib.pyplot as plt


def bollinger_bands(df,lookback,plot='no'):
    sym = list(df.columns.values)[0]
    rolling_mean = df.rolling(window=lookback,center=False).mean()
    rolling_std = df.rolling(window=lookback,center=False).std()
    upper_band = rolling_mean + 2*rolling_std
    lower_band = rolling_mean - 2*rolling_std
    lower_band.rename(columns={sym:'lower band'}, inplace=True)
    upper_band.rename(columns={sym:'upper band'}, inplace=True)
    rolling_mean.rename(columns={sym:'SMA'}, inplace=True)

    if plot == 'yes':
        ax = df.plot(title="Bollinger Bands", label=sym,color = 'blue')
        rolling_mean.plot(ax=ax, color='gold')
        upper_band.plot(ax=ax, color = 'cyan')
        lower_band.plot(ax=ax, color = 'cyan')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left', prop={'size':8})
        plt.savefig(sym+'_BollingerBands.png')
        plt.show()
    return rolling_mean,upper_band,lower_band

if __name__ == '__main__':
    tickers = ['GILD','AAPL']
    shares = 100
    start = '2015-01-01'
    end = '2016-12-20'
    df = get_adjusted_close(tickers,start,end)
    lookback = 20
    for i in tickers:
        df1 = df[i].to_frame()
        bollinger_bands(df1,lookback,plot='yes')

