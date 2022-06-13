#변수
#연산자
# "+, - ,* , / ,% , **
#< , > , <= , >=

#파이썬에서 = 기호는 대입의 의미  

#오른ㅉ녹 데이터를 왼쪽 변수에 대입 

# R언어에서는 <- 로 표기 

#우측 데이터를 왼쪽에 할당한다. (대입) 


#R언어 에서는 <- 표기

#우측 데이터를 왼쪽에 할당 (대입 .assignment) 

#식별자 , 객체명 , 변수명 , 대소문자 구분 숫자 사용 가능

a<-1
a 

#변수의 선언 및 데이터 할당 
#R 벡터 : 여러 요소를 담는 데이터 형태 1차원
#정수형 벡터/실수형 벡터/문자형 벡터/ 논리형 벡터
#벡터 생성 :  c키워드 사용 

y<-c(1,2,3,4) 

y 

#데이터 프레임 생성

x<- data.frame(id=1:3, name=c("A","B","C"), logic=c(TRUE,FALSE,TRUE))

x
(class)x
attributes(x)

x<-c('m', 'f' , 'f' ,'m', 'f' ,bigender)

typeof (x)
x2 <- factor(x)
x2
#factor 요인
#factor는 문자로 된 범주형 정보로 저장하여
#분석하는데 사용한다.

#np.nan / null/ Nan
# R언어의 NaN

#not a number
#NA : not available 정의되지 않은 값.
#NAN : not a number
x<-c(NaN,NA)
x

is.na(x)
is.nan(x)

#R의 내장 함수 
# 데이터 분석을 위한 수치 관련 함수가 포함 .
#round()함수
#mean()함수
#abs()함수 절댓값 absolute 

round(2.583840)
mean(c(1,3,5))

x<-1:20
x
mean(x)

round(mean(x))
abs(-3)


#사용자 정의 함수 (내가 만드는 함수 )
#함수의 구성 방법
#function_name 함수명
#함수가 호출될 때의 매개변수
#함수의 수행문

#xx<-function(x,y)
#{
#   수행문
#}

#floor() 내림
#round() 반올림
#cos() sin() tan()
#log()
#median() 중위값
#sum() 합계
#min() 최소 
#max() 최대
#range(x) 범위 생성

xy<-function(x,y)
{
  y<-x^2+y^2
  return(y)
}
xy(x=2,y=3)
# ^ 제곱
# 함수 안에서 return장용

#1~50 포함 벡터  c가벡터
a<-c(1,2,3,4,5)
b<-c(1:50)
a
b

dice<-function()
{
  x<-1:6
  y<-sample(x,size=2)
  sum(y)
}
dice()

#무작위로 랜덤 뽑는 함수
#size = 몇 개 

#R 언어에도 조건문이 있다.

#if (조건)
#{
# 조건이 참일때 실행문
#}
#else
#{
#  거짓일 때 실행
#}  

x<-c(-3:3)

ifelse(x %% 2==0, "짝수", "홀수")  #(앞이참 뒤가거짓) x를 2로 나누면 0이면 짝 R만있는 문법
z<-ifelse(x%%2==0,"짝", "홀")
xz<- data.frame(x,z)
xz

x<- -5:5
z<- ifelse(x %% 5==0,y<-"zero",ifelse(x %% 5==1,y<-"one", ifelse(x %% 5==2,y<-"two", ifelse(x %% 5==3, y<-"three", ifelse(x %% 5==4, y<-"four",y<-"value")))))
z

xz<-data.frame(x,z)
xz

#R언어의 반복문
#for while
# for 문법 구성 방법
#for ( i in data ) { 반복 수행문}

for(x in 1:10)
{
  y<-10*x
  print(y)
}  

y
#while문
#while(참or거짓){if{break}}
#탈출: break
#처음으로 반복: next

j<-1
while (TRUE) 
{
  j<-j+3
  if(j>20)
  {
    j<-1
    break
    
  }
}

j

#repeat 반복문
#repeat{if() break}
#repeat은 무조건 반복, 탈출 조건이 없어 if조건으로 break를 설정해야 함

k<-1
repeat
{
  k <- k+5
  if(k>25)
    {
     break
  }
}
k















 

 
      
      
