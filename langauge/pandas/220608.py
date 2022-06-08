
#22.06.08 판다스


 #1.    1차원 데이터 구조 series    2차원 데이터 구조 dataFrame
 #2.    2차원 데이터 구조 데이터 프레임
 # 판다스는 여러 영역에서 데이터 분석에 사용된다.


#판다스는 여러 영역에서 데이터 분석에 사용된다.

#시리즈는 동일한 데이터 타입을 저장하고 있는 1차원 배열
# 데이터 프레임은 레이블화 되어 있는 2차원 자료 구조로 서로 다른 타입의 여러 칼럼으로 구성.




import numpy as np
import pandas as pd

sdata=[2000.0, 3000.0, 4000.0, np.nan]
city = ['서울', '부산', '울산' , '목포']
print(sdata)
myseries2 = pd.Series(sdata,index=city)
myseries2.name='호호호'
myseries2.index.name='크크크'
print(myseries2)



print(list(range(3)))

myseries1= pd.Series(range(0,4))
print("1", myseries1)
myseries1 = pd.Series(sdata,index=city)

myseries22=pd.Series([4,5,6])
print("2",myseries22)



myseries3=pd.Series([4,5,6])
index=['a','b','c']
myseries33 = pd.Series(sdata,index=city)
print("3",myseries3)
print("3",myseries33)

sdata={ '서울':3000, '부산':2000}
myseries4 =pd.Series (sdata)
print("4 ",myseries4)
myseries4 = pd.Series(sdata,index=city)

#딕셔너리 , range 객체 리스트를 시리즈 자료형으로 변환


myindex= ['서울', '부산', '광주', '대구', '울산', '목포', '여수']
mylist= [50, 60, 40, 80, 70, 30, 20]
myseries = pd.Series(data=mylist, index= myindex)
print(myseries)


#myseries의 대구 인데스값이 출력.

print(myseries[['대구']])
print(myseries['대구':'목포'])  #대구 ~ 목포

print(myseries[['대구','목포']])  # 대구, 목포 끝

print(myseries[[2]])

print(myseries[0:5:2])  #0에서부터 인덱스 5까지 2칸간격씩 출력한다.

print(myseries[3:6])  #3이상 6미만



# 인데스 변경
myseries[2] =22
myseries[2:5] =33

(myseries[['서울', '대구']])= 55

(myseries[0::2])=89   # :: 끝까지    0번부터 끝까지 2칸마다

print(myseries)


#데이터 프레임
#2차원 형태의 표구조를 가지는 자료형태
#행과 열에 대한 인덱스를 가지고 순서대로 출력
#열 1개 가 하나의 series가 된다.


sdata= {'city':['서울','서울','서울','부산','부산'],
        'year':['2000','2001','2002','2001','2002'],
        'pop': [1.5,1.7,3.6,2.4,2.9]
    }
print(sdata,"\n")

df = pd.DataFrame(sdata)
print("df출력",df)

mycolumn = ['city','year','pop'] #컬럼
myindex= ['one','two','three','four','five']

myframe= pd.DataFrame( sdata,columns=mycolumn, index= myindex)
print(myframe)


#데이터 프레임은 행 구분자를 의미하는 색인
#열 구분자를 의미하는 라벨과 자료로 구성

#라벨: 자료는 열로 구성되고 각 열은 이름을 가진다. 위 예시에서 city,year, pop.
#인덱스 : 위 예시에서 one two three ....
#자료: 자료는 리스트 튜플 딕셔너리 등으로 주어질 수 있다.


#DataFrame 생성할 때 매개 변수
# 1.data : 데이터 프레임으로 만드려는 대상 데이터 (딕셔너리 배열 리스트 시리즈 )
# 2.index : 인덱스 지정 (기본값은 0부터 자동 배치)
# 3.columns : 열의 제목
# 4.dtype : 데이터의 형태 (자동으로 지정)
# 5.copy : 자료의 copy 여부 결정 True/False 값 입력
#예시 Dataframe( data= none, index= none , column= none ,dtypes= none, copy= none)


mylist= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
mylist2= list(5*data for data in range(1,26))
print(mylist)
print(mylist2)

myindex=['이순신','김유신','강감찬','광해군','연산군']
mycolumns=['서울','부산','광주','목포','경주']

arr= np.reshape(mylist2, (5,5))
print(type(arr))
print(arr)


df= pd.DataFrame(arr,index= myindex, columns=mycolumns)  #pd. Dataframe  (데이터함유한 자료구조, index(행) 가로부제부여
#                                                        , column(열) 세로부제지정
print(df)

#데이터 프레임 생성할 때 데이터에 컬럼이 포함되어 있지 않으면 columns 속성에 추가가능
#넘파이의 ndarray 데이터만 포함하고 있음.


#iloc함수

#행 인덱스 번호를 기준으로 행을 추출해주는 함수
result =df.iloc[1]  # 0~ N행중 1행 출력  1행의 1,2,3,4,(열값 + 데이터) 처음부터~ 끝행까지 로 출력
print(type(result))
print(result)

result= df.iloc[[1,3]]  # 1~ 2까지의 행출력  1이상 3미만. frame으로 출력 범위출력해야되니. 1개만 series  2개이상= DF.
print(type(result))
print(result)

#데이터 프레임에서 행 추출을 통해 1개의 행을 추출하면 시리즈로 변환
#데이터 프레임 에서 행 추출을 통해 2개이상의 행을추출하면 DataFrame으로 반환


result=df.iloc[0::2]    #0 ~ 끝까지 행중  2줄씩!! 나눠서 출력  :: =전체
print(type(result))
print(result)


#loc 은 라벨을 이용한 행 추출
result=df.loc['김유신']  #iloc 에서 loc만씀 이순신행의 열만 추출
print(type(result))
print(result)

result=df.loc[['김유신']]    # [[김유신]] 대괄호로 묶이면 이안의 모든것들!!
print(type(result))
print(result)

# 1개의 행일 때  대괄호를 2개 사용하면 Dataframe 형태로 반환한다.

result=df.iloc[[1,0]]
print(type(result))
print("iloc출력 \n",result)  #iloc 행을 한줄씩 다출력가능!! 마지막열까지 출력됨

result=df.loc[['김유신','이순신']]
print(type(result))
print(result)



print("행name출력 ",df.index)
#df.index 데이터 프레임의 인덱스 항목 객체 반환 프로퍼티
mytarget=np.random.choice(df.index,3) #행의 3개 랜덤으로 출력
print(mytarget)
#np.random.choice() 함수
#넘파이 패키지의 랜덤 모듈의 초이스 함수
#df.index 객체의 항목 중 3개를 뽑는다.
print(type(mytarget))
#그 반환 형태는 넘파이의 array 형태


result=df.loc[mytarget]
print(result)
print(type(result))
#df.index객체를 loc 속성에 대입하여 특정 행만 추출

#[행], [열] 행태로 데이터 추출 가능
result= df.loc[['강감찬'],['광주']]
print(result)
print(type(result))

#복수의 행, 열 형태 데이터 추출

result= df.loc[ ['연산군', '강감찬'] ,['광주', '목포']]
print(result)
print(type(result))

result= df.loc['김유신':'광해군','광주': '목포']
print(result)
print(type(result))

result= df.loc['김유신':'광해군',['부산']]
print(result)
print(type(result))

#False/ True로 데이터 추출 방법

result=df.loc[[False,False,False,False,True],['부산', '서울']] # 마지막 행만 True로 출력!
print(result)

print(df)


result=df.loc[df['부산']<=100]
print(result)

print(df['목포'])
print(type(df['목포']))

result=df.loc[df['목포']==120]
print(result)


print(df['목포']==120)
#비교 연산자 적용 반환 값은 True or False값을 가진 시리즈



#학생 10명에 대한 데이터 프레임을 생성하는데 
#index 학생명 가명으로
#col 연락처 나이 성별 
# 성별 0여자 1남자 , 점수 1~100
sna=['김또깡','박승지','박승주','박승호','박승미','박승구','김승지','정승지','도승지','하승지']

# sge=['0','0','1','1','0','0','1','0','0','1']
solI=['나이','성별','나이','성별','나이','성별','나이','성별','나이','성별']
sol=['15','16','14','18','21','23','25','22','32','47','0','0','1','1','0','0','1','0','0','1','15','16','14','18','21','23','25','22','32','47','0','0','1','1','0','0','1','0','0','1'
     ,'15','16','14','18','21','23','25','22','32','47','0','0','1','1','0','0','1','0','0','1'
     ,'15','16','14','18','21','23','25','22','32','47','0','0','1','1','0','0','1','0','0','1'
     ,'15','16','14','18','21','23','25','22','32','47','0','0','1','1','0','0','1','0','0','1']

# df= pd.DataFrame(sol,index= solI, columns=sna)
# print(df)




sna=['김또깡','박승지']

# sge=['0','0','1','1','0','0','1','0','0','1']
solI=['나이','성별']
sol=['15','16','1','0']




arr= np.reshape(sol, (2,2))
print(type(arr))
print(arr)


df= pd.DataFrame(arr,index=solI, columns=sna)
print(df)

result=df.iloc[1]
print(result)