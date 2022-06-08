
import time as t
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#
# listbox.select_set(0)
#     listbox.event_generate("<<ListboxSelect>>")

x= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.melon.com/index.htm'
url2= 'https://www.naver.com/'
xpath1='/html/body/div[2]/div[2]/div/div[2]/ul[1]/li[3]/a/span[2]'
xpath2='/html/body/div[2]/div[3]/div/div/div[5]/form/div/table/tbody/tr[2]/td[5]/div/div/div[2]/a'

xpath3='//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a'
xpath4='/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a'

x.get(url2)
b= x.find_element(by=By.CLASS_NAME, value="nav_item")
print("클래스 nav_item명",b.text)

# a= x.find_element(by=By.XPATH, value=xpath)
# instead

# Please use find_element(by=By.CLASS_NAME, value=name)
t.sleep(2)
a = x.find_element(by=By.XPATH, value=xpath3)
a.click()


b = x.find_element(by=By.XPATH, value=xpath4)
b.click()
t.sleep(2)
print(a)
# driver.find_element(by=)
while True:
    pass