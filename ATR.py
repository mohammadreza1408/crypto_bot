import sys
import time
import requests
import ccxt
import pandas as pd
from datetime import datetime


def atr(symbol):
    time.sleep(15)
    exchange = ccxt.kucoin()
    bars = exchange.fetch_ohlcv(f'{symbol}', timeframe='1d', limit=11)  # Daily candles ten days before the currency
    

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 500)
    #
    df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close',
                                          'volume'])  

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  
    df['previous_close'] = df['close'].shift(1)  # The value of the previous close candle

    def tr(df):  
        df['high-low'] = df['high'] - df['low']
        df['high-pc'] = abs(df['high'] - df['previous_close'])
        df['low-pc'] = abs(df['low'] - df['previous_close'])
        tr = df[['high-low', 'high-pc', 'low-pc']].max(axis=1)
        return tr

    def ATR(df, period=10):  
        df['tr'] = tr(df)
        the_atr = df['tr'].rolling(period).mean()  
        df['atr'] = the_atr


    ATR(df, period=10)  

    atr_value = df['atr'].iloc[-1] 

    
    atr_percent_A_line = (float(atr_value) * 10) / 100
    atr_percent_C_line = (float(atr_value) * 15) / 100
    return atr_percent_A_line,atr_percent_C_line


