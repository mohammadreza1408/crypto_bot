# Pivots are calculated
from datetime import datetime

def calculat_newyork_first_candle(data_Klines):# Extraction of New York 9 AM candles
    time_newyork_list = []
    for i in range(len(data_Klines)):
        timestamp = int(data_Klines[i][0])
        dt_obj = datetime.fromtimestamp(timestamp).strftime('%H-%M-%S')
        if dt_obj == '09-00-00': 
            time_newyork_list.append(data_Klines[i])
    return time_newyork_list
    





def Calculate_One_day_Pivot(get_klines_24h): #Daily candle calculation
    
    _24klines = get_klines_24h  # Last 24 candles in 72 hours
    high_daily_list = []
    low_daily_list = []
    for i in range(len(_24klines)):
        high_daily_list.append(_24klines[i][3])  # Shadow above 24 candles
        low_daily_list.append(_24klines[i][4])  # Shadow down 24 candles
    daily_max = float(max(high_daily_list))  # The biggest shadow above
    daily_min = float(min(low_daily_list))  # The smallest shadow below
    daily_close = float(_24klines[0][2])  # Close the last candle

    x = (daily_max + daily_min) / 2
    y = (daily_max + daily_min + daily_close) / 3
    w = abs(x- y)
    pivot_low = y - w
    pivot_high = y + w
    return pivot_high, pivot_low


def Calculate_Three_Days_Pivot(get_klines_72h): # 3-day candle calculation
    high_three_day_list = []
    low_three_day_list = []
    for i in range(len(get_klines_72h)):
        high_three_day_list.append(get_klines_72h[i][3]) 
        low_three_day_list.append(get_klines_72h[i][4])
    three_day_max = float(max(high_three_day_list)) 
    three_day_min = float(min(low_three_day_list)) 
    three_day_close = float(get_klines_72h[0][2]) 



    x= (three_day_max + three_day_min ) / 2
    y = (three_day_max + three_day_min + three_day_close) / 3
    w = abs(y - x)
    pivot_low = y - w
    pivot_high = y + w
    return pivot_high, pivot_low





