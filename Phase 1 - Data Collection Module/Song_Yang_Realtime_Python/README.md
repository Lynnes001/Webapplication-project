# Python Web Crawler for Historical Stock Data (1 year) on Yahoo Finance using BeautifulSoup and Selenium

# Before you run:
  **PLEASE MAKE SURE YOU HAVE ALREADY INSTALLED 'pip' for Python!**
  * Environment:
    + Python 2.7
    + Jupyter Notebook:
      > pip install jupyter notebook

    + Ubuntu(not required)

  * Dependencies:

    + request 2.8
      > pip install requests

--------------------------------------------------------------------------------

# How to run:
  * Get data of your stock:
    - Read the 'Examples' section in the code.
    - Get the stock code of your stock, e.g., Google: GOOG, Yahoo: AABA, etc.
    - Say you want to get the company example's stock, whose stock code is 'CODE':
      > Example: getRealtimeStock("stock symbol"):

    - Retrieve data:
      > res: Store all current information
        res[0]: Stock Symbol
        res[1]: Stock Name
        res[2]: Stock Current price
        res[3]: Current timestamp
    **For Details Please Read the Code**

_Created and tested on Mar.1.2018 by Song Yang (sy540)
