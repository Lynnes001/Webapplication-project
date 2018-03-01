
# coding: utf-8

from urllib import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import time

# call selenium and chromedriver to get driver
def driveChrome(url):
    driver = webdriver.Chrome('/Users/yx960203/Desktop/chromedriver') # CHANGE THE DRIVER TYPE and PATH HERE!!

    # mimic mouse operation to scroll down and show the full page
    driver.get(url)
    driver.execute_script("window.scrollBy(0,3000)")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(0.1)

    return driver

# resolve html to soup
def getSoup(url, driver):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(driver.page_source, "lxml")
    return soup;

def getHistoricalData(url):
    driver  = driveChrome(url)
    soup = getSoup(url,driver)
    # get dates
    days = soup.find_all("td", class_ = "Py(10px) Ta(start) Pend(10px)") # <td class="Py(10px) Ta(start) Pend(10px)"><span>Feb 28, 2018</span></td>
    dates = []
    for day in days:
        dates.append(day.text)

    # get prices and volume
    elements = soup.find_all("td", class_ = "Py(10px) Pstart(10px)") # <td class="Py(10px) Pstart(10px)"><span>1,123.03</span></td>

    openp = [] # open price
    highp = [] # high price
    lowp = [] # low price
    closep = [] # close price
    adjclosep = [] # adjusted close price
    volume = [] # volume

    counter = 0
    for element in elements:
        #print(element.text)
        text = element.text.replace("," , "")
        counter+=1;
        if counter % 6 == 1:
            openp.append(float(text))
        elif counter % 6 == 2:
            highp.append(float(text))
        elif counter % 6 == 3:
            lowp.append(float(text))
        elif counter % 6 == 4:
            closep.append(float(text))
        elif counter % 6 == 5:
            adjclosep.append(float(text))
        elif counter % 6 == 0:
            volume.append(int(text))
    tmp = [dates, openp, highp, lowp, closep, adjclosep, volume]
    res = np.stack(tmp,axis = 1)

    return res

def getURL(stockCode):
    return "https://finance.yahoo.com/quote/"+ stockCode + "/history?p=" + stockCode


# ------------------------------- ** Examples ** --------------------------------------

"""
Example: example = getHistoricalData(getURL("yourStockCode"))


example: records of all year
example[x]: record of day x from today

example[x][0]: date (String)
example[x][1]: open price (float)
example[x][2]: high price (float)
example[x][3]: low price (float)
example[x][4]: close price* (float)
example[x][5]: adjusted close price** (float)
example[x][6]: volume (int)

Index from 0 to 251(252 total).
0   is the most recent day(Feb.28.2018)
251 is the least recent day(Mar.01.2017)
Tested Feb.28.2018 by Xin Yang.

*Close price adjusted for splits. **Adjusted close price adjusted for both dividends and splits.
"""

google = getHistoricalData(getURL("GOOG"))

print len(google) # record numbers
#print google
print google[0] # first record
print google[251] # last record
print google[0][1] # date of first record

yahoo = getHistoricalData(getURL("AABA"))

print len(yahoo)
print yahoo[0]
print yahoo[251]
