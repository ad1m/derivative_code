from Portfolio_Constructor import *
import numpy as np

def cumulative_returns(df):
    return (df[-1]/df[0])-1

def daily_returns(df):
    dr = (df/df.shift(1)) - 1
    dr = dr[1:]
    return dr

def average_daily_returns(df):
    dr = daily_returns(df)
    return dr.mean()

def volatility(df):
    dr = daily_returns(df)
    return dr.std()

def Sharpe_Ratio(df,rf=0):
    samples_per_year = 252
    mean_avg_daily_rets = (average_daily_returns(df) - rf).mean()
    vol = volatility(df)
    sharpe_ratio = np.sqrt(samples_per_year)*(mean_avg_daily_rets/vol)
    return sharpe_ratio

def BTR(pv,comp,start,end,shares,cash,rf=0):
    tickers = [comp]
    comp_adj_close = get_adjusted_close(tickers,start,end)
    comp_pv = Portfolio_Value(comp_adj_close,shares,cash)
    comp_returns = daily_returns(comp_pv)
    port_returns = daily_returns(pv)
    covariance = np.cov(port_returns,comp_returns)[0][1]
    variance = np.var(comp_returns)
    beta = covariance/variance
    Treynor_Ratio = (cumulative_returns(pv) - rf)/beta
    return beta,Treynor_Ratio

if __name__ == '__main__':
    tickers = ['AAPL','BAC','GILD','MSFT']
    start = '2014-01-01'
    end = '2016-01-01'
    cash = 100000
    shares = [100,100,100,100]
    df = get_adjusted_close(tickers,start,end)
    pv = Portfolio_Value(df,shares,cash)
    cr = cumulative_returns(pv)
    dr = daily_returns(pv)
    adr = average_daily_returns(pv)
    vol = volatility(pv)
    sr = Sharpe_Ratio(pv)
    b,tr = BTR(pv,'SPY',start,end,[sum(shares)],cash)
    print 'Cumulative Return: ' + str(cr) +'\n'
    print 'Daily Returns: \n'
    print dr
    print '\n'
    print 'Average Daily Return:' + str(adr) + '\n'
    print 'Volatility: ' + str(vol) + '\n'
    print 'Sharpe Ratio: ' + str(sr) + '\n'
    print 'Beta: ' + str(b) + '\n'
    print 'Treynor Ratio: ' + str(tr) + '\n'

    #Treynor Comparison
    tickers = ['SPY']
    shares = [400]
    df = get_adjusted_close(tickers,start,end)
    pv = Portfolio_Value(df,shares,cash)
    b,tr = BTR(pv,'SPY',start,end,shares,cash)
    print 'SPY Treynor Ratio: ' +str(tr)