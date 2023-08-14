


def Grayd_of_Risk(ACD_or_candles,ONE_day_pivot,THREE_day_pivot):
    if ACD_or_candles['OR_L'] > ONE_day_pivot[0] and ONE_day_pivot[1] >= THREE_day_pivot[0] :

        return 'low ==> long_position'
    if ACD_or_candles['OR_L'] > ONE_day_pivot[0] and ONE_day_pivot[0] > THREE_day_pivot[0] :
        return 'medium ==> long_position'
    if ACD_or_candles['A_down'] > THREE_day_pivot[1] and ACD_or_candles['A_down'] < THREE_day_pivot[0]: 
        if ONE_day_pivot[0] > THREE_day_pivot[0]:
            return 'Pivot trade ==> long_position'

    return 'high ==> long_position'


