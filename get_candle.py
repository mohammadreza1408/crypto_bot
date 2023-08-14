import asyncio
import time
from datetime import datetime
import requests
from calculate_pivote import calculat_newyork_first_candle
from calculate_pivote import Calculate_One_day_Pivot,Calculate_Three_Days_Pivot
from ATR import atr
import logging
from trade_Risk import Grayd_of_Risk

logging.basicConfig(level=logging.INFO,filename='LOG.log',format='%(asctime)s-- %(funcName)s -- %(levelname)s -- %(message)s')

# market = 'ADA-USDT'
# tick_interval = '5min' #1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week
url = 'https://api.kucoin.com'


market = 'PAXG-USDT'

tick_interval = '1hour'
# tick_interval = '30min'
headers = {'Connection': 'close'}
response1= requests.session().get(url + f'/api/v1/market/candles?type={tick_interval}&symbol={market}',headers=headers,timeout=5,stream=True, )
data_Klines = response1.json()
response1.close()
print("data_Klines :",data_Klines)
start_timstamp_list = calculat_newyork_first_candle(data_Klines['data'])
first_timestamp = start_timstamp_list[0][0]

start_timstamp = start_timstamp_list[3][0] 


print("***" *50)
print("start_timstamp_list :",start_timstamp_list)
print("first_timestamp :",first_timestamp)
print("start_timstamp :",start_timstamp)
print("***" * 50)




time.sleep(15)
response2 = requests.session().get(url + f'/api/v1/market/candles?type={tick_interval}&symbol={market}&startAt={start_timstamp}',headers=headers,timeout=5, stream= True)
get_klines = response2.json()
response2.close()
get_klines_72h = get_klines['data'][-72:]
get_klines_24h = get_klines_72h [0:24]
#
one_day_pivot = Calculate_One_day_Pivot(get_klines_24h)
three_day_pivot = Calculate_Three_Days_Pivot(get_klines_72h )
atr_number = atr(market)
print("one_day_pivot :",one_day_pivot)
print("three_day_pivot :",three_day_pivot)
print("ATR_A_AND_C :",atr_number)

_30min_timestamp = int(first_timestamp) + 1800 
print("sleep Dovom")

response3= requests.session().get(url + f'/api/v1/market/candles?type=30min&symbol={market}&startAt={start_timstamp}&endAt={_30min_timestamp}',headers=headers,timeout=5,stream=True)
_30min_klines = response3.json()
response3.close()
print('_30min_klines :',_30min_klines)

OR_H= float(_30min_klines['data'][0][3])
OR_L= float(_30min_klines['data'][0][4])
A_up= OR_H + atr_number[0]
A_down = float(abs(OR_L -atr_number[0]))
C_up= OR_H + atr_number[1]
C_down= float(abs(OR_L - atr_number[1]))


ACD_OR_candles ={
   'symbol':market,
   'OR_H': OR_H,
   'OR_L':OR_L,
   'A_up':A_up,
   'A_down':A_down,
   'C_up':C_up,
   'C_down':C_down
}
print(ACD_OR_candles)
grade = Grayd_of_Risk(ACD_OR_candles,one_day_pivot,three_day_pivot)
print("risk_level is: ",grade)

logging.info( f'\n on_day_pivot :{one_day_pivot}\n three_day_pivot :{three_day_pivot} \n '
             f'ATR_A_AND_C :{atr_number} \n ACD_OR_candles : {ACD_OR_candles}')
logging.info("\n =========================================================================================")