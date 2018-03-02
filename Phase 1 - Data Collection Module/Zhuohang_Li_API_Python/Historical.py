from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import sys

for stockSymbol in sys.argv[1:]:
    ts = TimeSeries(key='0345Y49CIQ03XJK3', output_format='pandas')  # replace YOUR_API_KEY with your key
    data, meta_data = ts.get_daily(symbol=stockSymbol, outputsize='compact')
    print('Processing '+stockSymbol)
    pprint(data.tail(1))
    data.to_csv(stockSymbol + '_history.csv', index=True, sep=',')