
from  selenium import webdriver
import time as t

# x= webdriver.ChromeOptions()
# x.add_argument("headless")
# x.add_argument('window-size = 1920x1080')
# browser = webdriver.Chrome("chromedriver.exe", options=x)
# browser.get("https://www.melon.com/")


x= webdriver.Chrome("chromedriver.exe")

url=("https://www.melon.com/")
x.get(url)



#페이지 열림 완료 시점
#
 #2초의 텀을준다.
#프레임전환

#프레임 전환을 해야한다.!! iframe 으로 프레임이 바꼈으므로
# x.switch_to.frame("searchIframe")

#menu_bg menu01 #멜론차트 클래스 불러오기
a= x.find_element_by_class_name("menu_bg") #
print(a.text)
a.click()
t.sleep(1)

x.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #스크롤 내리기 함수


# /html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[98]/td[6]/div/div/div[1]/span/a

xpath1="/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr["
xpath2= input("몇등곡?")
xpath3="]//td[6]/div/div/div[1]/span/a"




# /html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[100]/td[6]/div/div/div[1]/span/a
xpath100=xpath1+xpath2+xpath3

print(xpath2,"위곡")
print(x.find_element_by_xpath(xpath100).text)


print("두번째 출력")
# print(x.find_element_by_class_name("ellipsis").text)

t.sleep(1)

# y=x.find_element_by_css_selector(".ellipsis > span > a")
# print(y)
# print(type(y))
# print(len(y))
# x.quit()

# song_name= x.find_element("Christmas Tree")
song_name= x.find_element_by_xpath("/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[100]/td[6]/div/div/div[1]/span/a")

print(song_name)
webdriver.ActionChains(x).context_click(song_name).perform()


# Context click #우클릭 매뉴  액션 사용



get_title = x.title
# Printing the title of this URL
# Here it is null string
print(get_title, " ", len(get_title))

# Opening the website
# x.get(url) 첫화면 불러오기
# Getting current URL source code

# Printing the title of this URL
