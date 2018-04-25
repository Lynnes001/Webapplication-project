from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys
import os

if not os.path.exists('./data'):
    os.mkdir("data")

def get_historical_data(stockSymbol):
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=stockSymbol, outputsize='full')
    data.to_csv('./data/' + stockSymbol + '_history.csv', index=True, sep=',')

def get_macd(stockSymbol):
    ti = TechIndicators(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ti.get_macd(symbol=stockSymbol, interval='daily', series_type='close')
    data.to_csv('./data/' + stockSymbol + '_macd.csv', index=True, sep=',')

def get_stoch(stockSymbol):
    ti = TechIndicators(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ti.get_stoch(symbol=stockSymbol, interval='daily')
    data.to_csv('./data/' + stockSymbol + '_stoch.csv', index=True, sep=',')

def get_obv(stockSymbol):
    ti = TechIndicators(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ti.get_obv(symbol=stockSymbol, interval='daily')
    data.to_csv('./data/' + stockSymbol + '_obv.csv', index=True, sep=',')

def get_ema(stockSymbol):
    ti = TechIndicators(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ti.get_ema(symbol=stockSymbol, interval='daily', series_type='close')
    data.to_csv('./data/' + stockSymbol + '_ema.csv', index=True, sep=',')

def get_rsi(stockSymbol):
    ti = TechIndicators(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=stockSymbol, interval='daily', series_type='close', time_period='60')
    data.to_csv('./data/' + stockSymbol + '_rsi.csv', index=True, sep=',')

def get_cci(stockSymbol):
    ti = TechIndicators(key='0345Y49CIQ03XJK3', output_format='pandas')
    data, meta_data = ti.get_cci(symbol=stockSymbol, interval='daily', time_period='60')
    data.to_csv('./data/' + stockSymbol + '_rsi.csv', index=True, sep=',')


for stockSymbol in sys.argv[1:]:
    print('Processing ' + stockSymbol)
    get_historical_data(stockSymbol)
    get_macd(stockSymbol)
    get_stoch(stockSymbol)
    get_obv(stockSymbol)
    get_ema(stockSymbol)
    get_rsi(stockSymbol)
    get_cci(stockSymbol)
