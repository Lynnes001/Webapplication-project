from alpha_vantage.timeseries import TimeSeries
import numpy as np

""" take the stock symbol as parameter,
    return the latest up-to-time data as list,
    with the format of: [timestamp, open, high, low, close, volume]
"""
def get_latest(symbol):
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='full')
    a=list(data.tail(1).index)
    b=np.array(data.tail(1)).tolist()
    c=[b[0][0],b[0][1],b[0][2],b[0][3],b[0][4]]
    a.extend(c)
    return a


""" return the data within last 10 days(default)/1 year that has the highest 'high' value,
    with the format of: [timestamp, open, high, low, close, volume]
"""
def get_high(symbol, period='10days'):
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    if(period=='10days'):
        slice=data.tail(10)
    if(period=='1year'):
        slice=data.tail(365)
    sorted=slice.sort_values(by='2. high')
    a=list(sorted.tail(1).index)
    b=np.array(sorted.tail(1)).tolist()
    c=[b[0][0],b[0][1],b[0][2],b[0][3],b[0][4]]
    a.extend(c)
    return a


""" return the data within last 10 days(default)/1 year that has the lowest 'low' value,
    with the format of: [timestamp, open, high, low, close, volume]
"""
def get_low(symbol, period='10days'):
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    if(period=='10days'):
        slice=data.tail(10)
    if(period=='1year'):
        slice=data.tail(365)
    sorted=slice.sort_values(by='3. low')
    a=list(sorted.head(1).index)
    b=np.array(sorted.head(1)).tolist()
    c=[b[0][0],b[0][1],b[0][2],b[0][3],b[0][4]]
    a.extend(c)
    return a


""" return average close value of last 10 days(default)/1 year
"""
def get_avg(symbol, period='10days'):
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    if(period=='10days'):
        slice=data.tail(10)
    if(period=='1year'):
        slice=data.tail(365)
    print(slice)
    close=slice['4. close']
    return close.mean()
