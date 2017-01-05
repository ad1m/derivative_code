__author__ = 'Adamlieberman'
from urllib2 import Request,urlopen
import time

'''
 Code for Scraping Fundamental Data Blog Post
'''
def fundamental_scraper(tickers,metrics):
    d = {'bid':'b','close':'p','open':'o','dividend_yield':'y','dollar_change':'c1','percent_change':'p2',
         'days_low':'g','days_high':'h','1_year_target_price':'t8','200_day_ma_dollar_change':'m5',
         '200_day_ma_percent_change':'m6','50_day_ma_dollar_change':'m7','50_day_ma_percent_change':'m8',
        '200_day_ma':'m4','50_day_ma':'m3','revenue':'s6','52_week_high':'k','52_week_low':'j','52_week_range':'w',
         'market_cap':'j1','float_shares':'f6','name':'n','symbol':'s','exchange':'x','shares_outstanding':'j2',
         'volume':'v','ask_size':'a5','bid_size':'b6','last_trade_size':'k3','average_daily_volume':'a2','eps':'e',
         'current_eps_estimate':'e7','next_year_eps_estimate':'e8','next_quarter_eps_estimate':'e9','book_value':'b4',
         'ebitda':'j4','price_to_sales':'p5','price_to_book':'p6','pe':'r','peg':'r5','short_ratio':'s7'}
    if metrics == 'all':
        vals = d.values()
        metrics = d.keys()
    else:
        vals = [d[i] for i in metrics]
    f1 = open('fundamental_metrics.txt','w')
    d1 = {}
    d2 = {}
    count = 1
    for i in range(len(tickers)):
        f1.write(tickers[i]+'\n')
        for j in range(len(metrics)):
            req_link = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (tickers[i], vals[j])
            req = Request(req_link)
            resp = urlopen(req)
            content = resp.read().decode().strip()
            f1.write(metrics[j]+': '+str(content)+'\n')
            d2[metrics[j]] = content
        d1[tickers[i]] = d2
        d2 = {}
        f1.write('\n')
        count = count+1
        if count %50 == 0:
            time.sleep(10)
    f1.close()

    return d1

if __name__ == '__main__':
    tickers = ['AAPL','GILD','MSFT']
    metrics = ['pe','peg','average_daily_volume','eps']
    #metrics = 'all'
    f = fundamental_scraper(tickers,metrics)
    print f
    print f['AAPL']['peg']

