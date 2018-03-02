
# coding: utf-8

# In[26]:


import sys 
sys.path.append('Xin_Yang_Historical_Python')
sys.path.append('Song_Yang_Realtime_Python')
sys.path.append('SQL')

import time
import os
import multiprocessing

from Xin_Yang_Historical_Data import getHistoricalData, getURL
from Song_Yang_Realtime_Data import getRealtimeStock
from mysql_functions import dbInsertStock, dbInsertRealTime, dbInsertHistoryTime


# In[27]:


def RealtimeStock(StockName):
    name = multiprocessing.current_process().name
    print name, 'Starting'
    while 1:
        realtimeInfo = getRealtimeStock(StockName)
        print realtimeInfo
        dbInsertRealTime(realtimeInfo)
        time.sleep(1)
        
def StopRealtimeStock(RealtimeStockService):
    name = multiprocessing.current_process().name
    print name, 'Exiting'
    RealtimeStockService.terminate()
    print 'TERMINATED:', RealtimeStockService, RealtimeStockService.is_alive()
    RealtimeStockService.join()
    print 'JOINED:', RealtimeStockService, RealtimeStockService.is_alive()
    
def main(argv1, argv2):
    runtime = argv2
    stockname = argv1
    RealtimeStockService = multiprocessing.Process(name='RealtimeStockService', target=RealtimeStock(stockname))
    RealtimeStockService.start()
    print 'DURING:', RealtimeStockService, RealtimeStockService.is_alive()
    time.sleep(float(runtime))
    StopRealtimeStock(RealtimeStockService)


# In[28]:


# realtime 60s
if __name__ == '__main__':
    main(str(sys.argv[1]), str(sys.argv[2]))