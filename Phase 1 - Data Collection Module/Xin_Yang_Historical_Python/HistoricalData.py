from urllib import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
url = "https://finance.yahoo.com/quote/GOOG/history?p=GOOG"

driver = webdriver.Chrome('/Users/yx960203/Desktop/chromedriver')
driver.get(url)
driver.execute_script("window.scrollBy(0,3000)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(1)

response = urlopen(url)
html = response.read()
soup = BeautifulSoup(driver.page_source, "lxml")

elements = soup.find_all("tr", class_ = "BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)")
res = []
for element in elements:
    print(element.text)
    res.append(element.text.split(","))
#print(res)