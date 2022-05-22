#업비트 가격 불러오기


from  selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
x= webdriver.Chrome("chromedriver.exe")

url=("https://www.bithumb.com/")
x.get(url)
#페이지 열림 완료 시점
#
 #2초의 텀을준다.
#프레임전환

#프레임 전환을 해야한다.!! iframe 으로 프레임이 바꼈으므로
# x.switch_to.frame("searchIframe")


#on main_menu_list
a= x.find_element_by_xpath("/html/body/div[4]/header/div/div[2]/div/div/ul[1]/li[1]/a") #
print(a.text)
a.click()
t.sleep(1)

b = x.find_element_by_xpath("/html/body/div[3]/section/div[2]/div[1]/div[2]/div/div/div[1]/ol/li[1]") #
print(b.text)
b.click()
t.sleep(1)



# driver.switch_to.default_content() 스위치 처음창으로 돌아가기
# last_height = x.execute_script("return document.body.scrollHeight") #스크롤 높이 확인
# print(last_height)


element = x.find_element(By.ID,"aside_coin")  #webdriver.ActionChains.scroll()
x.switch_to.window(element)
x.execute_script("scrollbot.scrollTo(0, document.body.scrollHeight);") #끝까지내리기
webdriver.ActionChains(x).scroll(0, 0, 0,100000000 , origin=element).perform()  #맨아래내리기


#모든 코인 시세 확인
# a1= x.find_element(by=By.XPATH, value=("/html/body/div[4]/section/div[2]/div[1]/div[2]/div/div/div[1]/ol"))
# print(a1.text)

xpath= "/html/body/div[3]/section/div[2]/div[1]/div[2]/div/div/div[1]/ol/li["
xpath1= input("몇번째로 거래량높은 코인 선택할껀가?(내림차순) ")
xpath2= "]"
xpath100=xpath+xpath1+xpath2

print(xpath1,"선택 crypto")
print(x.find_element(by=By.XPATH, value=xpath100).text)

# <div class="scrollbot-scrollbar-holder" style="width: 3px; height: 100%; right: 0px; top: 0px;"><div class="scrollbot-scrollbar" style="width: 3px; height: 9.8683%; right: 0px; top: 0%;"></div></div>  #스크롤 요소


#시장가 구매
#tradingview_766cd
# x.switch_to.frame("tradingview_766cd")
c1= x.find_element(by=By.XPATH, value= "/html/body/div[3]/section/div[2]/div[2]/article/div[3]/dl/dd/form/table[1]/tbody/tr[1]/td/div/span[2]/label/span[2]") #

# "/html/body/div[4]/section/div[2]/div[2]/article/div[3]/dl/dd/form/table[1]/tbody/tr[1]/td/div/span[2]/label"
print(c1.text)
c1.click()
t.sleep(1)



# 구매할 자금입력
c2= x.find_element(by=By.XPATH, value="/html/body/div[4]/section/div[2]/div[2]/article/div[3]/dl/dd/form/table[1]/tbody/tr[8]/td/div[1]/input") #

# "/html/body/div[4]/section/div[2]/div[2]/article/div[3]/dl/dd/form/table[1]/tbody/tr[1]/td/div/span[2]/label"
print(c2.text)
c2.click()
t.sleep(1)
# driver.find_element_by_name('username').send_keys('아이디 입력')
# driver.find_element_by_name('password').send_keys('비밀번호 입력')


# <div class="tx_l tx_link">이더리움<span class="coinSymbol sort_coin" data-sorting="이더리움">ETH/KRW</span> <span class="blind">ETHEREUM이더리움</span></div>
#/html/body/div[4]/section/div[2]/div[1]/div[2]/div/div/div1]/ol/li[2]/a/div[1]

#/html/body/div[3]/section/div[2]/div[1]/div[2]/div/div/div[1]/ol/li[2]/a/div[1]/span[1] #이더
# <div class="tx_l tx_link">이더리움<span class="coinSymbol sort_coin" data-sorting="이더리움">ETH/KRW</span> <span class="blind">ETHEREUM이더리움</span></div> xpath소스
# <div class="tx_l tx_link">이더리움<span class="coinSymbol sort_coin" data-sorting="이더리움">ETH/KRW</span> <span class="blind">ETHEREUM이더리움ㅇㄷㄹㅇ</span></div>

# <span class="coinSymbol sort_coin" data-sorting="이더리움">ETH/KRW</span> 이더 요소복붙
# /html/body/div[3]/section/div[2]/div[1]/div[2]/div/div/div[1]/ol/li[1]  #이클  xpath소스