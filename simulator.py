__author__ = 'Adamlieberman'
import csv
from Portfolio_Constructor import *
from performance_metrics import *

def simulate(orders,start,end,starting_capital):
    symbols = []
    reader = csv.reader(open(orders,'rU'),delimiter=',',quoting=csv.QUOTE_NONE)
    ls_orders = [[x.strip() for x in row] for row in reader]
    ls_orders.pop(0) #removing header
    for i in ls_orders:
        symbols.append(str(i[1]))
    dates = pd.date_range(start, end)
    tickers = list(set(symbols))
    df = get_adjusted_close(tickers,start,end)
    df['cash'] = 1.0
    df_trades = df.copy()
    df_trades[:] = 0
    for i in ls_orders:
        date = pd.to_datetime(str(i[0]))
        if date in dates:
            symbol = i[1]
            trade = i[2]
            shares = int(i[3])
            if trade == 'SELL':
                shares = shares*-1
            df_trades[symbol][date] = df_trades[symbol][date]+shares
            df_trades['cash'][date] = df_trades['cash'][date] + -1*(df_trades[symbol][date])*df[symbol][date]
        df_holdings = get_adjusted_close(tickers,start,end)
        df_holdings['cash'] = 1.0
        df_holdings[:] = 0
        df_holdings['cash'][start] = starting_capital
        for i in ls_orders:
            date = str(i[0])
            date = pd.to_datetime(date)
            if date in dates:
                symbol = i[1]
                df_holdings[symbol][date] = df_holdings[symbol][date]+df_trades[symbol][date]
                df_holdings['cash'][date] = df_holdings['cash'][date] + -1*(df_holdings[symbol][date]*df[symbol][date])
        df_holdings = df_holdings.cumsum()
        df_value = df_holdings*df
        portvals = df_value.sum(axis=1)
    return portvals

if __name__ == '__main__':
    f = 'Orders/orders.csv'
    start = '2011-01-05'
    end = '2011-12-20'
    starting_capital = 100000
    pv = simulate(f,start,end,starting_capital)
    print pv
    cr = cumulative_returns(pv)
    dr = daily_returns(pv)
    adr = average_daily_returns(pv)
    vol = volatility(pv)
    sr = Sharpe_Ratio(pv)
    print '------- Performance -------\n'
    print 'Cumulative Return: ' + str(cr) +'\n'
    print 'Daily Returns: \n'
    print dr
    print '\n'
    print 'Average Daily Return:' + str(adr) + '\n'
    print 'Volatility: ' + str(vol) + '\n'
    print 'Sharpe Ratio: ' + str(sr) + '\n'