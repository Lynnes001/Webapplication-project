from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import time
import sys
import pandas as pd
from sqlalchemy import create_engine

# stockSymbol=sys.argv[1]
# while(True):
#     ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas') #replace YOUR_API_KEY with your key
#     data, meta_data = ts.get_intraday(symbol=stockSymbol, interval='1min', outputsize='full')
#     pprint(data.tail(1))
#     # save to mysql
#     # engine = create_engine('mysql+mysqldb://root:password@localhost:3306/databasename?charset=utf8')
#     # pd.io.sql.to_sql(data.tail(1), 'tablename', engine, schema='databasename', if_exists='append')
#     time.sleep(60)

for stockSymbol in sys.argv[1:]:
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')  # replace YOUR_API_KEY with your key
    data, meta_data = ts.get_intraday(symbol=stockSymbol, interval='1min', outputsize='full')
    print('Processing '+stockSymbol)
    pprint(data.tail(1))
    data.to_csv(stockSymbol + '.txt', index=True, sep=' ')
