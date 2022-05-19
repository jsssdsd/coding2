import matplotlib.pyplot as plt


#pyplot 모듈은 함수의 모음
#그래프을 만들 수 있다.

import numpy as np
#일반적으로 maplot 사용시 numpy array(배열)을 이용한다.
#재료로 numpy array (배열)을 넣지 않아도 내부적으로 np.array로 자동 변환됨
#튜플 딕셔, 리스트 다가능
font1={'family':'serif',
       'color':'b',
       'weight':'bold',
       'size':20
}






x=np.arange(6)


# 17	0	28	6	20	2
# 발생건수	사망자수	부상자수	중상	경상	부상신고
plt.rcParams["font.family"]='Malgun Gothic'
aciN=['발생건수','사망자수','부상자수','중상','경상','부상신고']
value=[17,0,28,6,20,2]
colors=['#221123','#1313f2','#6313f2','#1313f2','#1313f2','#1312f2']
plt.ylim([0,28])
plt.bar(aciN,value,color=colors)   #바에 x,y값지정
plt.title("서울 종로구 뺑소니 교통사고수 ")
plt.ylabel("건수")
plt.xlabel("분류")
plt.show()



#years는 x축에 표시되는 연도
#value는 막대 그래프의 값

# plt.barh(x,aciN)  #x축 눈금 레이블에 연도가 표시됨
# plt.yticks([])
# plt.xticks(aciN)