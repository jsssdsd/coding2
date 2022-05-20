from datetime import datetime
def currentTime():
    dt = datetime.now()
    print("현재시간: %s : %s" %(dt.hour,dt.minute))

def calTimeToEnd():
    userinput=input("오늘 수업이 끝나는 시각을 입력하세요. ex)5시50분의 경우 17,50으로 입력 ")
    userinputlist=userinput.split(',')
    for i in range(len(userinputlist)):
        if userinputlist[i].isdigit():
            dt = datetime.now()

            if dt.hour > int(userinputlist[0]) and dt.minute > int(userinputlist[1]):
                print("오늘 수업은 이미 끝났습니다.")
                return
            else:
                time_1 = datetime.strptime(str(dt.hour)+':'+str(dt.minute)+':'+str(dt.second), "%H:%M:%S")
                time_2 = datetime.strptime(userinputlist[0]+':'+userinputlist[1], "%H:%M")

                time_difference = time_2 - time_1
                print('수업 종료까지 남은 시간:%s' %time_difference)


                return
        else:
            print("시간 입력 오류.")
            return

#currentTime 함수는 매개변수 없음 / 현재시간을 출력하는 함수
#calTimeToEnd 함수는 현재시간으로부터 수업 종료 시간까지 남은 시간을 계산하는 함수






