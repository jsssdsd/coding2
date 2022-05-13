
import time

# 데이터 전처리 모듈
import raw_data_to_list as rl
post=rl.postData()

# 해당 모듈의 재료들
temp_list = []
ex_page = 0

class postClass:
    def __init__(self,postNum,ID,contents,time,secret,nick,num):
        self.postNum=postNum
        self.contents=contents
        self.time=time
        self.ID=ID
        self.secret=secret
        self.nick = nick
        self.num=num

def search_keyword(a):
    post = rl.postData()
    temp_list=[]
    for i in range(len(post)):
        if a in post[i][2]:
            temp_list.append(post[i])

    if not temp_list:
        print('검색된 내용이 없습니다.')
        return

    temp_list.reverse()
    return temp_list

def search_follow(user):
    import follow_module as fm

    post = rl.postData()
    temp_list = []
    if fm.checkFollowlist(user):
        temp_1= fm.checkFollowlist(user)
        for i in range(len(post)):
            for m in range(len(temp_1)):
                if  temp_1[m] in post[i][1]:
                    temp_list.append(post[i])
        if not temp_list:
            return
        temp_list.reverse()
        return temp_list
    else:
        return
def search_post(postNumlist):
    post = rl.postData()

    temp_list = []

    for i in range(len(post)):
        for m in range(len(postNumlist)):
            if postNumlist[m] == post[i][0]:
                temp_list.append(post[i])

    if not temp_list:
        print('검색된 내용이 없습니다.')
        return

    return temp_list

def search_id(a):
    post = rl.postData()

    temp_list = []

    for i in range(len(post)):
        if a == post[i][1]:
            temp_list.append(post[i])

    if not temp_list:
        print('검색된 내용이 없습니다.')
        return

    temp_list.reverse()
    return temp_list

def search_all():
    import raw_data_to_list as rl
    post = rl.postData()

    temp_list = []

    for i in range(len(post)):
        temp_list.append(post[i])

    if not temp_list:
        return

    temp_list.reverse()
    return temp_list

def search_someone(userClass):
    import raw_data_to_list as rl
    post = rl.postData()

    temp_list = []
    for i in range(len(post)):
        if userClass.id == post[i][1]:
            temp_list.append(post[i])
    if not temp_list:
        return
    temp_list.reverse()
    return temp_list


def class_list(list_data):
    classList=[]
    for i in range(len(list_data)):
        globals()['p_{}'.format(i+1)]=postClass(list_data[i][0],list_data[i][1],list_data[i][2],list_data[i][3],list_data[i][4],list_data[i][5],i+1)
        classList.append(globals()['p_{}'.format(i+1)])
    return classList

def show_page(classList,pageLimit=4):
    global temp_1
    exList=len(classList)%pageLimit
    temp_1=[]
    maxPage=len(classList)//pageLimit
    if exList == 0:
        pass
    else:
        maxPage+=1

    # pageLimit 기준으로 묶어주기.
    if exList == False:
        for i in range(maxPage): # 3 / 0~2
            temp_2=[]
            for m in range(pageLimit): # 4 / 0~3
                temp_2.append(classList[i*pageLimit+m]) #
            temp_1.append(temp_2)
    else:
        for i in range(maxPage-1):  # 2 // 0~1
            temp_2 = []
            for m in range(pageLimit):  # 4 / 0~3
                temp_2.append(classList[i * pageLimit + m])
            temp_1.append(temp_2)
        cL=classList[-exList:]
        temp_1.append(cL)

    # 묶인 리스트 표현
    temp_3=[]
    sel_page=1
    for i in range(len(temp_1[sel_page-1])):
        temp_3.append(temp_1[sel_page-1][i])
    return (temp_3,maxPage,temp_1)


def sel_others(sel_page,maxPage):
    global temp_1
    temp_3 = []
    for i in range(len(temp_1[sel_page-1])):
        temp_3.append(temp_1[sel_page-1][i])
    return (temp_3, maxPage)

def sel_follow(temp_list,sel_page):
    temp_4 = []
    for i in range(len(temp_list[sel_page-1])):
        temp_4.append(temp_list[sel_page-1][i])
    return temp_4


if __name__=="__main__":
    print('페이지 검색기')

