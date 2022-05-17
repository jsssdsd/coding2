
from  selenium import webdriver
import time as t

x= webdriver.Chrome("chromedriver.exe")

x.get("https://map.naver.com/v5/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90?c=14180705.8225507,4349362.5731894,14,0,0,0,dh")

#페이지 열림 완료 시점
#


t.sleep(2)  #2초의 텀을준다.
#프레임전환
#프레임 전환을 해야한다.!! iframe 으로 프레임이 바꼈으므로
x.switch_to.frame("searchIframe")

#_3Apve

a= x.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[3]/form/div/table/tbody/tr[1]/td[6]/div/div/div[1]/span/a")
print(a.text)

# a= x.find_element_by_class_name("_3Apve")
# print(a.text)  # a의 텍스트를 따온다.