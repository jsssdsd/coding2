#클래스
#class

#절차지향 프로그래밍 언어 : c언어.
#객체지향 프로그래밍 언어 : 파이썬, 자바스크립트

#클래스는 꼭 필요하지는 않다.
result= 0

class Calculator:  #클래스 정의
    #클래스의 정의 : 틀을 만드는 것
    def __init__(self):   #기본 문법
        self.result=0 #객체변수 self.
    def add(self,num):  #덧셈
        self.result+=num
        return self.result
    def minus(self,num):  #뺄셈
        self.result-=num
        return self.result
    def multi(self, num): #곱셈
        self.result*=num
        return self.result
    def divide(self, num): #나눗셈
        self.result/=num
        return self.result

c1=Calculator()  #c1에 계산기가 들어간다. #c1객체 생성 cal 클래스를 이용해서 만듬
c2=Calculator() #계산기의 복사.  #c2객체 생성 : cal 클래스 를 이용해서 만듬
c3=Calculator() #같은 클래스로 생성한 객체끼리 독립적이다.
print(c1.add(5))
print(c2.add(10))
print(c3.add(3))
print(c1.add(3))
print(c2.add(10))
print(c1.minus(5))

print("="*100)
print(c1.result)
print(c2.result)
print(c3.result)


#클래스 =과자 틀
class cookie:
    pass

ck1= cookie()#객체명 ck1
ck2= cookie()

#객체는 클래스의 인스턴스이다.
#클래스: 틀
#클래스로 만든 객체를 인스턴스라고도 한다.
#ck1객체는 cookie클래스의 인스턴스

#ck1은 객체이다.
#ck1은 쿠키클래스의 인스턴스

class FourCal:
    lastname = '김' # 클래스변수.
    def __init__(self,x,y): #생성자 메서드. #객체 생성과 동시에 실행.
        self.first=x
        self.second=y
    def setdata(self,x,y): #3개의 입력값을 받는다.  #setdata로 변수값지정.
        self.first=x  #변수 선언.
        self.second=y
    def add(self):
        result=self.first+self.second  #변수는 임의로 생성 무한히 가능.
        return result
    def minu(self):
        result=self.first-self.second  #변수는 임의로 생성 무한히 가능.
        return result
    def multiplication(self):
        result=self.first*self.second  #변수는 임의로 생성 무한히 가능.
        return result
    def divis(self):
        result=self.first/self.second  #변수는 임의로 생성 무한히 가능.
        return result

# #클래스 내부의 함수는 메서드라고 표현한다.
# print("nnnnnnnnnn")
# a=FourCal()   #a는 fourcal 클래스의 인스턴스이다.  용어 이해.  (클래스=과자틀, 인스턴스 =과자)  창조자와 피조물
# print(type(a))
# x= 10
# print(type(x))
# print(a.setdata(4,2))  #   a = self
# #첫 매개변수 self는 특별한 기능이 있다.                                               #파이썬조작법 crtl 움직이면서 shft 로 지정.

#setdata 메서드의 첫 매개변수 self에는 setdata메서드를 호출한
#객체 a가 자동으로 전달 된다.

# __init__ 메서드
#생성자 메서드


a=FourCal(4,5)
print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
print(a.first)
print(a.second)
b=FourCal(40,50)
b.setdata(400,500)
print(b.first)
print(a.add())


#클래스의 상속.
#물려받기


class FourCal2(FourCal): #Fourcal2 에 Fourcal1를 상속해줬다.
    def pow(self):       #Fourcal의 함수가 5개가됨.! 기존의 4개에 1개를 내가 추가했다.!! 내입맛대로
        result=self.first**self.second
        return  result

x=FourCal2(10,20)
print(x.first)
print(x.add())


#왜 상속을 하는가?
#기존 클래스를 보존하면서
#기존 클래스의 기능에 변경이나 추가를 원한다면 상속한다.
print(x.pow())

#라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황.
#메서드 오버라이딩

class F3(FourCal):  #상속받은클래스 = 자식클래스. 상속해준클래스= 부모
    def add(self):
        print("123123123")

v=F3(20,10)

print(v.first)
print(v.second)
print(v.add())

print('n'*100)
print(v.add())
print(FourCal.add(v))  #오버라이딩 되지전의 함수를 불러쓰는법.
print(FourCal2.divis(v))
# a= FourCal  #클래스 사용법11@@@@@@@@@@
# FourCal.add(a) #222222


#부모클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을
#메서드 오버라이딩(덮어쓰기)라고 한다.
#이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신
#오버라이딩한 메서드가 호출된다.


#클래스 변수

class Family:
    lastname='박'
    def __init__(self,x,y):
        self.a=x
        self.b=y

F1=Family(10,20)
F2=Family(40,50)

print(F1.a,F1.b,Family.lastname)  #객체객체 클래스
print(F2.a,F2.b,F2.lastname)  #객체 객체 클래스.

print(id(F1.lastname))
print(id(F2.lastname))
print(id(F1.a))
print(id(F2.a))


#클래스 변수 접근방법
#1.객체명. 클래스변수명
#2.클래스명.클래스변수명

#클래스 함수 호출 방법
#1. 객체명.메서드명
#2. 클래스명. 메서드명

#클래스변수는 공용.
#바뀌지않는값 클래스변수 , 안의 기능값 객체변수, 객체안의 세부기능 메서드.

#문제1 #은행계좌 account
#속성: 예금주명/잔액/은행/계좌번호/
#1. 공통속성: 클래스 변수
#2.객체속성: 객체변수

#기능: 입금/출금/잔액확인
#생성자 메서드 구현

