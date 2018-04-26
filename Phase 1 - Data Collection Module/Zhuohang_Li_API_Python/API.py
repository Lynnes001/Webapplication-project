from alpha_vantage.timeseries import TimeSeries
import numpy as np

""" take the stock symbol as parameter,
    return the latest up-to-time data as list,
    with the format of: [timestamp, open, high, low, close, volume]
"""
def get_latest(symbol):
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='full')
    a=list(np.array(np.array(data.tail(1).index)))
    b=np.array(data.tail(1)).tolist()
    c=[b[0][0],b[0][1],b[0][2],b[0][3],b[0][4]]
    a.extend(c)
    return a