# Webapplication-project
This is the first Project Phase 1 - Data Collection Module (Group Task). We implemented following two program.

- Python Web Crawler for Historical Stock Data
- Python Realtime Stock Data on Yahoo Finance using Http Request

You will see program Readme.md in folders.

# General Instruction
  * Environment:
    + Python 2.7
    
    + Google Chrome
    
    + Jupyter Notebook:
      > pip install jupyter notebook

    + MacOS/Ubuntu(not required)

#### For realtime data program

  * Dependencies:
    + MySQLdb:
      > pip install mysqldb-python
      
    + request 2.8
      > pip install requests
      
#### For historical data program

  * Dependencies:
    + MySQLdb:
      > pip install mysqldb-python
      
    + numpy:
      > pip install numpy

    + Beautiful Soup:
      > pip install beautifulsoup4

    + Selenium 3.9
      > pip install -U selenium
        or
      > pip install selenium

    + chromedriver:
      Download drivers for your browsers: https://pypi.python.org/pypi/selenium/

#### Build Database:
1. Login to mysql as root
2. Load stockDB.sql
    > Mysql>source <Fullpath.sql> 
   - Example: 
        >Mysql>source D:\test\ss.sql
        
    * If failed, you can try following steps
```MySQL 
CREATE DATABASE stockDB;
USE stockDB;

CREATE TABLE Real_Time_Data(
    rid INT UNSIGNED AUTO_INCREMENT NOT NULL,
    symbol VARCHAR(4) NOT NULL,
    stock_time DATETIME,
    price FLOAT,
    volume INT,
    PRIMARY KEY(rid)
);

CREATE TABLE History_Time_Data(
    hid INT UNSIGNED AUTO_INCREMENT NOT NULL,
    symbol VARCHAR(4) NOT NULL,
    stock_date DATE,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    adj_close FLOAT,
    volume INT,
    PRIMARY KEY(hid)
);

```
