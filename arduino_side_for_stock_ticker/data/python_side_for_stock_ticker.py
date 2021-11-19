import yfinance as yf
import time
import serial as seri
StockShares = ['DOW','YHOO','BAC','F','JPM','TWTR','CHK','PBR','FIT','COG','ABX','FCX','GE','TRGP','CNX','BSX','MRC','NKE','NEM','PBRA','HST','BP','MRK','HON','MET','CLR','WPX' \
,'EXC','JCP','YELP','GNC','TSLA','VRX','P','NFLX','CMG','SM','WYNN','SHAK','ICON']

ser = seri.Serial('COM7',9600)
def printShare(share,name):
    ser.write(name + ': *' + share.info['regularMarketPrice'])
    print(f"name + ': *' + {share.info['regularMarketPrice']}")
    time.sleep(.1)
def mainProgram():
    for i in StockShares:
        name = i
        s = yf.Ticker(i)
        printShare(s,name)
        s.refresh()
        time.sleep(9.5)
    mainProgram()
mainProgram()


    # shib = yf.Ticker('SHIB-USD')
    # shib_price = pd.to_numeric(shib.info['regularMarketPrice'])
    # if shib_price != 
    # shib_price = format(shib_price, '.10f')
    # shib_price
    # print(shib_price)
    # time.sleep(3)