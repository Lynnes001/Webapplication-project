
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


RealtimeStockService.terminate()
print 'TERMINATED:', RealtimeStockService, RealtimeStockService.is_alive()

