__author__ = 'Adamlieberman'
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

def get_adjusted_close(tickers,start,end):
    d = {} #our dictionary
    for ticker in tickers:
        d[ticker] = web.DataReader(ticker,"yahoo",start,end)
    pan = pd.Panel(d)
    df_adj_close = pan.minor_xs('Adj Close')
    return df_adj_close

def Portfolio_Value(df_adj_close,shares,cash):
        total_shares = float(sum(shares))
        weights = [w/total_shares for w in shares]
        normed = df_adj_close/df_adj_close.ix[0,:]
        alloced = normed*weights
        pos_vals = alloced*cash
        series_portfolio_value = pos_vals.sum(axis=1)
        return series_portfolio_value


def Plot_Portfolio_Value(port_val,show='no'):
    plt.style.use('ggplot')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Portfolio Value')
    ax.set_ylabel('Portfolio Value ($)')
    port_val.plot()
    if show == 'yes':
        plt.show()
    plt.savefig('Portfolio_Value.png')
    return


def plot_stocks(stocks,show='no'):
    plt.style.use('ggplot')
    stocks.plot()
    plt.title('Stock Performance')
    plt.ylabel('Stock Price')
    plt.xlabel('Date')
    plt.legend(loc='upper left', prop={'size':6}, bbox_to_anchor=(1,1))
    plt.tight_layout(pad=7)
    if show == 'yes':
        plt.show()
    plt.savefig('stock_performance.png')
    return


if __name__ == '__main__':
    tickers = ['AAPL','BAC','GILD','MSFT']
    start = '2014-01-01'
    end = '2016-12-21'
    df_adj_close = get_adjusted_close(tickers,start,end)
    print df_adj_close
    plot_stocks(df_adj_close,show='yes')
    weights = [100,100,100,100]
    cash = 100000
    port_val = Portfolio_Value(df_adj_close,weights,cash)
    print port_val
    Plot_Portfolio_Value(port_val,show='yes')