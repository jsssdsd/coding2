import matplotlib.pyplot as plt


#pyplot 모듈은 함수의 모음
#그래프을 만들 수 있다.

# plt.plot([1,2,3,4]) #그래프를 만드는 과정
# plt.show()#그래프 출력
#
# plt.plot([1,2,3,4],[5,10,15,20]) #첫번째 리스트 x축  두번쨰 y축
# plt.show()
#
# plt.plot([1,2,3,4],[5,10,15,20],'ro') # red
# plt.axis([0,4,0,20]) #xmin, xmax, ymin, ymax
# plt.show()

import numpy as np
#일반적으로 maplot 사용시 numpy array(배열)을 이용한다.
#재료로 numpy array (배열)을 넣지 않아도 내부적으로 np.array로 자동 변환됨
#튜플 딕셔, 리스트 다가능
font1={'family':'serif',
       'color':'b',
       'weight':'bold',
       'size':20
}
arr=np.arange(0.,5.,0.2) #start stop step
print(arr)
print(type(arr))

# plt.plot(arr,arr,'r--',arr,arr**2,'bs',arr,arr**3,'g^')
plt.show()


# plt.plot((1,2,3,4,5,6,7))
plt.show()

#딕셔너리로 plot 생성

# data= {'data_x':[1,2,3,4,5], 'data_y': [2,3,4,10,8]}
# plt.plot('data_x','data_y',data=data)
# plt.xlabel('firstLable',labelpad=10,fontdict=font1)
plt.show()
#matplotlib. pyplot 에서 plot의 재료로
#튜플리스트 ndarray 딕셔너리 사용가능r

#축 레이블 설정
#x축과y축에 레이블 설정가능

# plt.plot([1,2,3,4],[1,4,8,10])
# plt.xlabel("xxxx",labelpad=10)
# plt.ylabel("yyyy",labelpad=2)
plt.show()

#레이블 폰트 지정 방법
# plt.plot([1,2,3,4], [1,4,8,200])
# plt.xlabel('firstLable',labelpad=10,fontdict={'family':'serif','color' :'b', 'weight':'bold','size':30})
plt.show()

#폰트 미리 지정

font1={'family':'serif',
       'color':'b',
       'weight':'bold',
       'size':20
}


#레이블 위치 조절

# plt.plot([1,2,3,4],[2,5,8,9])
# plt.xlabel('XXX',loc='right')#X축 레이블 위치는 레프트 라이트 센터
# plt.ylabel('YYY',loc='top')#y축 레이블 위치는 바텀, 탑, 센터
plt.show()


#범례 표시(legend)
#데이터의 종류를 표시하는 텍스트
# plt.plot([1,2,3,4],[2,5,7,100],label='Price')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()


#범례의 위치조절
# plt.plot([1,2,3,4],[2,5,7,100],label='Price')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=(1.0,1.0))
# plt.show()


#속성값으로 범례 위치 조정
# plt.plot([1,2,3,4],[2,5,7,100],label='Price')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc='lower right')
# plt.show()

#범례 수 지정

#
# plt.plot([1,2,3,4],[2,3,4,10],label='Price')
# plt.plot([1,2,3,4],[3,5,9,6],label='Human')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc='best',ncol=1,fontsize=20)
# plt.show()


# plt.plot([1,2,3,4],[2,3,4,10],label='Price')
# plt.plot([1,2,3,4],[20,100,1000,0.0001],label='Luna')
# plt.plot([1,2,3,4],[1,65.33,887,123],label='enhwa')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc='best',ncol=2,fontsize=10,frameon= True,shadow=True)  #ncol2 =열2개
# plt.show()
#frameon 파라미터는 상자의 테두리 표시여부 True
#shadow는 상자의 그림자 여부


#축의 범위 지정 xlim ylim

# plt.plot([1,2,3,4],[2,3,4,10])
# plt.xlabel('x')
# plt.xlabel('y')
#
# plt.xlim([0,5]) #x축의 범위[xmin, xmax] 리스트나 튜블로 입력
# plt.ylim([0,20])
#
# plt.show()

#
# #축의 옵션 설정
#
# plt.plot([1,2,3,4], [2,3,5,10])
# plt.xlabel('hello')
# plt.ylabel('hi')
# plt.axis('scaled') #x축과 y축이 같은 길이 스케일로 매핑된다.
# # on / off /equal/ scaled/ tight/auto/normal 등등...
#

plt.show()




#그래프의 선 종류 지정

plt.plot([1,2,3,4],[4,4,4,4],'-',color='#e35f62',label='solid',linewidth=10, solid_capstyle='round')
plt.plot([1,2,3,4],[3,3,3,3],'--',color='limegreen',label='Dashed')
plt.plot([1,2,3,4],[2,2,2,2],':',color='red',label='Dotted')
plt.plot([1,2,3,4],[1,1,1,1],'-.',color='green',label='Dash-dot')
plt.xlabel('Xlabelllllllllll')
plt.ylabel('Ylabelllllllllll')
plt.axis([0.8,3.2,0.5,5.0])
plt.legend(loc='upper right',ncol=4)
plt.show()




#그래프의 특정 영역 채우기
#fill_between(x[:],y[:]) - 두 수평 사이의 곡선 사이를 채운다.
#fill_between() - 두 수평 사이의 곡선 사이를 채운다.

#fill_between()사용예
#
# x=[1,2,3,4,]
# y=[2,3,5,10]
#
# plt.plot(x,y)
# plt.xlabel('x')
# plt.xlabel('y')
#
# plt.fill_between(x[1:3],y[1:3],alpha=0.5)
# plt.show()
#
#
# #fill_betweenx()
# x=[1,2,3,4,]
# y=[2,3,5,10]
#
# plt.plot(x,y)
# plt.xlabel('x')
# plt.xlabel('y')
#
# plt.fill_betweenx(y[2:4],x[2:3],alpha=0.5)
# plt.show()
#
#
# x=[1,2,3,4]
# y1=[2,3,5,10]
# y2=[1,2,4,8]
#
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.xlabel('x')
# plt.ylabel('x')
# plt.fill_between(x[1:3],y1[1:3],y2[1:3], color='lightgray',alpha=0.1)
# plt.show()


#fill() 사용예

x= [1,2,3,4]
y1=[2,3,5,10]
y2=[1,2,4,8]

# plt.plot([1,2,3,4],[2,3,4,10],label='Price')
# plt.plot([1,2,3,4],[3,5,9,6],label='Human')

plt.plot(x,y1, label='SQL')
plt.plot(x,y2)
plt.xlabel("xxxxxx")
plt.ylabel("yyyyyyyyyyy")
plt.fill([1.9,1.9,3.1,3.1],[1.0,4.0,6.0,3.0], color= 'red',alpha=0.3)
plt.title("gragh_XXXXXXXXXXXX")
plt.axis([1,12.2,1,15.0])
plt.legend(loc='upper right',ncol=4)
# plt.legend(loc='best',ncol=2,fontsize=10,frameon= True,shadow=True)  #ncol2 =열2개
plt.show()



#바 차트 생성

#수평으로 늘어나는  바차트
x=np.arange(3)
years=['2020','2021','2022']
value=[570,330,920]
plt.bar(x,years)   #y축 지정
plt.barh(x,value)  #x축
# plt.yticks([])

plt.show()
#years는 y축에 바그래프목록이름
#value는 x축이 데이터값


#수직으로 상승하느 바차트
x=np.arange(3)
years=['2020','2021','2022']
value=[570,330,920]
plt.bar(x,value)   #y축 지정 그래프
plt.barh(x,years)  #x축 눈금 레이블에 연도가 표시됨
# plt.yticks([])

plt.show()
#years는 x축에 표시되는 연도
#value는 막대 그래프의 값




# 바차트 yticks
x=np.arange(0,2,0.2)
plt.plot(x,x)
plt.plot(x,x**2)
plt.plot(x,x**3)

plt.xticks([0,1,2])
plt.yticks(np.arange(1,6))  #np. arange 눈금 설정
# xticks(np.arange(1,6)) 이면 x축의범위 1~5까지

plt.show()
#xticks는 x축 눈금  #yticks는 y축 눈금










