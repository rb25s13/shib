import yfinance as yf
import time
import serial as seri
import pandas as pd
StockShares = ['SHIB-USD','BTC-USD']
# ,'TSLA','LOTZ','UWMC','COMS'
# str(share.info["regularMarketOpen"]).encode()
ser = seri.Serial('COM7',9600)
def printShare(share,name):
    s_price = pd.to_numeric(share.info['regularMarketPrice'])
    s_price = str(format(s_price, '.10f'))
    ser.write(str(name).encode() + b'*' + str(s_price).encode())
    print(f"{name}: {s_price}")
    time.sleep(.1)
def mainProgram():
    for i in StockShares:
        name = i
        s = yf.Ticker(i)
        printShare(s,name)
        # s.refresh()
        # time.sleep(.5)
    mainProgram()
mainProgram()
