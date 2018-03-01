from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import time
import sys
import pandas as pd
from sqlalchemy import create_engine

stockSymbol=sys.argv[1]

while(True):
    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas') #replace YOUR_API_KEY with your key
    data, meta_data = ts.get_intraday(symbol=stockSymbol, interval='1min', outputsize='full')
    pprint(data.tail(1))
    # save to mysql
    # engine = create_engine('mysql+mysqldb://root:password@localhost:3306/databasename?charset=utf8')
    # pd.io.sql.to_sql(data.tail(1), 'tablename', engine, schema='databasename', if_exists='append')
    time.sleep(60)
