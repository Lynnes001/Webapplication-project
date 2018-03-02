# Webapplication-project
This is the first Project Phase 1 - Data Collection Module (Group Task). We implemented following two program.

- Python Web Crawler for Historical Stock Data
- Python Realtime Stock Data on Yahoo Finance using Http Request

You will see program Readme.md in folders.


# Instruction for background service Python Realtime Stock on Yahoo Finance.
  * Environment:
    + Python 2.7
    + Ubuntu(not required)

  * Dependencies:
    + MySQLdb:
      > pip install mysqldb-python
    + request 2.8
      > pip install requests
      
  * How to run    
    + `python RealtimeRun.py <StockSymbol> <runtime(min)>`
    + Example: the command will fetch AMZN realtime stock price for 10 minutes.
      > `python RealtimeRun.py AMZN 10`
