import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL='https://www.gopax.co.kr/exchange/btc-krw'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

react_id=driver.find_element_by_id("react")
print(react_id.text)

