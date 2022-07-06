import os
PPpath = os.getcwd()

def filecheck(listname):  #구인게시글목록, 구직게시글목록 파일 생성
    path = "%s.txt" % listname
    if os.path.isfile(path):
        pass
    else:
        list = open( "%s.txt" % listname, 'w', encoding='utf-8')
        list.write("")
        list.close()


def employer(title, writer, task, caution, price, place, phonenum, etc):  #구인 게시 글 작성
    erP = open("%s.txt" % (title + ' ' + writer), 'w', encoding='UTF-8')
    erP.write("제목: " + title + "\n")
    erP.write("글쓴이:" + writer + "\n")
    erP.write("해야할 일: " + task + "\n")
    erP.write("주의 사항: " + caution + "\n")
    erP.write("가격: " + price + "\n")
    erP.write("인수 장소 및 날짜&시간: " + place + "\n")
    erP.write("연락처: " + phonenum + "\n")
    erP.write("그 외 사항: " + etc)
    erP.close()

    list_erP = open("구인게시글목록.txt", 'a', encoding='UTF-8')
    list_erP.write(title + ' ' + writer + "\n")
    list_erP.close()



def employee(title, writer, time, preferTask, preferSize, area, phonenum):  #구직 게시 글 작성
    eeP = open("%s.txt" % (title + ' ' + writer),'w',encoding='UTF-8')
    eeP.write("제목:" + title + "\n")
    eeP.write("글쓴이:" + writer + "\n")
    eeP.write("가능한 날짜 및 시간대:" + time + "\n")
    eeP.write("선호하는 일:" + preferTask + "\n")
    eeP.write("선호하는 견종 사이즈:" + preferSize + "\n")
    #eeP.write("찾는 가격대:" + priceRange + "\n")
    eeP.write("가능한 지역:" + area + "\n")
    eeP.write("연락처: " + phonenum + "\n")
    eeP.close()

    list_eeP = open("구직게시글목록.txt", 'a', encoding='UTF-8')
    list_eeP.write(title + ' ' + writer + "\n")
    list_eeP.close()

l_e = []
def list(eeer):  #목록에서 원하는 글 선택 / 매개변수: 구인게시글목록 or 구직게시글목록
    global l_e
    list_erP = open("%s.txt" % eeer, 'r', encoding='UTF-8')
    l_e = l_e + list_erP.readlines()
    for i in range(len(l_e)):
        l_e[i] = l_e[i].replace("\n", '')
    list_erP.close()
    return l_e


post_l = []
def click(title):  #목록에서 선택된 글 불러오기
    global post_l
    post = open("%s.txt" % title, 'r', encoding='UTF-8')
    post_l = post_l + post.readlines()
    post.close()
    for i in range(len(post_l)):
        post_l[i] = post_l[i].replace("\n", "")
    return post_l

acc_info = []
def viewinfo(ID):  #회원정보 보기
    global acc_info
    post = open("회원정보.txt", 'r', encoding='UTF-8')
    infolist = post.readlines()
    post.close()
    del infolist[0]
    for i in range(len(infolist)):
        infolist[i] = infolist[i].replace('\n', '')
        infolist[i] = infolist[i].split('\t')
    for i in range(len(infolist)):
        if ID == infolist[i][0]:
            acc_info += infolist[i]
    return acc_info



def deletepost(title, eeer):  #게시글 삭제
    with open("%s.txt" % eeer, 'r', encoding='UTF-8') as list_eree:
        l_e = list_eree.readlines()
    with open("%s.txt" % eeer, 'w', encoding='UTF-8') as list_eree:
        for i in l_e:
            if i.strip("\n") != title:
                list_eree.write(i)
    os.remove("%s.txt" % title)
    os.remove("%s 댓글 목록.txt" % title)



def chEmployee(title, comment):  #댓글 선택시 나머지 삭제
    with open("%s 댓글 목록.txt" % title, 'w', encoding='UTF-8') as list_eree:
        list_eree.write(comment + '\n')



def rateEE(title, score):  #구인자 평가 및 회원정보에 반영
    with open("%s 댓글 목록.txt" % title, 'r', encoding='UTF-8') as ee:
        list = ee.readlines()
        list[0] = list[0].split('닉네임: ')
        list[0][1] = list[0][1].split(' /')

    nn = list[0][1][0]
    newinfo = ""
    with open("회원정보.txt", 'r', encoding='UTF-8') as info:
        infolist = info.readlines()

        for i in range(len(infolist)):
            infolist[i] = infolist[i].replace('\n','')
            infolist[i] = infolist[i].split('\t')
        for i in range(len(infolist)):
            if nn in infolist[i]:
                infolist[i][6] = float(infolist[i][6]) + 1
                infolist[i][5] = ((float(infolist[i][5]) * (float(infolist[i][6]) - 1)) +
                                  float(score))/float(infolist[i][6])
        for i in range(len(infolist)):
            infolist[i] = str(infolist[i][0]) + '\t' + str(infolist[i][1]) + '\t' + str(infolist[i][2]) + '\t' +\
                          str(infolist[i][3]) + '\t' + str(infolist[i][4]) + '\t' + str(infolist[i][5]) + '\t' +\
                          str(infolist[i][6]) + '\n'
        result = ''.join(map(str, infolist))
        newinfo += result

    with open("회원정보.txt", 'w', encoding='UTF-8') as changeinfo:
        changeinfo.write(newinfo)


def rateEE2(title, score):  #구직 글에서 구인자 평가 및 회원정보에 반영
    with open("%s.txt" % title, 'r', encoding='UTF-8') as ee:
        list = ee.readlines()
        list[1] = list[1].strip('글쓴이:')
        list[1] = list[1].strip('\n')

    nn = list[1]
    newinfo = ""
    with open("회원정보.txt", 'r', encoding='UTF-8') as info:
        infolist = info.readlines()

        for i in range(len(infolist)):
            infolist[i] = infolist[i].replace('\n','')
            infolist[i] = infolist[i].split('\t')
        for i in range(len(infolist)):
            if nn in infolist[i]:
                infolist[i][6] = float(infolist[i][6]) + 1
                infolist[i][5] = ((float(infolist[i][5]) * (float(infolist[i][6]) - 1)) +
                                  float(score))/float(infolist[i][6])
        for i in range(len(infolist)):
            infolist[i] = str(infolist[i][0]) + '\t' + str(infolist[i][1]) + '\t' + str(infolist[i][2]) + '\t' +\
                          str(infolist[i][3]) + '\t' + str(infolist[i][4]) + '\t' + str(infolist[i][5]) + '\t' +\
                          str(infolist[i][6]) + '\n'
        result = ''.join(map(str, infolist))
        newinfo += result

    with open("회원정보.txt", 'w', encoding='UTF-8') as changeinfo:
        changeinfo.write(newinfo)



def delcomt(title, sel):
    with open("%s 댓글 목록.txt" % title, 'r', encoding='UTF-8') as list_eree:
        l_e = list_eree.readlines()
    with open("%s 댓글 목록.txt" % title, 'w', encoding='UTF-8') as list_eree:
        for i in l_e:
            if i.strip("\n") != sel:
                list_eree.write(i)


def changeNNinlist(eree, nn , new):
    newinf = ''
    with open("%s.txt" % eree, 'r', encoding='UTF-8') as list:
        lr = list.readlines()
        for i in range(len(lr)):
            lr[i] = lr[i].split()
            if nn in lr[i]:
                lr[i][1] = new
        for i in range(len(lr)):
            lr[i] = lr[i][0] + ' ' + lr[i][1] + '\n'
        result = ''.join(map(str, lr))
        newinf += result
    with open("%s.txt" % eree, 'w', encoding='UTF-8') as list:
        list.write(newinf)
    newinf = ''



def changeallNN(nn, new):  #닉네임 변경시 모든 게시글, 댓글 제목/내용의 닉네임 변경
    path = 'C:/Users/202-8/PycharmProjects/pythonProjects - HJ/GroupProject/petPlatform'

    newinf = ''
    with open("구인게시글목록.txt", 'r', encoding='UTF-8') as list:
        lr = list.readlines()
        for i in range(len(lr)):
            lr[i] = lr[i].split()
            if nn in lr[i]:
                lr[i][1] = new
        for i in range(len(lr)):
            lr[i] = lr[i][0] + ' ' + lr[i][1] + '\n'
        result = ''.join(map(str, lr))
        newinf += result
    with open("구인게시글목록.txt", 'w', encoding='UTF-8') as list:
        list.write(newinf)
    newinf = ''
    with open("구직게시글목록.txt", 'r', encoding='UTF-8') as list:
        lr = list.readlines()
        for i in range(len(lr)):
            lr[i] = lr[i].split()
            if nn in lr[i]:
                lr[i][1] = new
        for i in range(len(lr)):
            lr[i] = lr[i][0] + ' ' + lr[i][1] + '\n'
        result = ''.join(map(str, lr))
        newinf += result
    with open("구직게시글목록.txt", 'w', encoding='UTF-8') as list:
        list.write(newinf)
    newinf = ''

    file_n = os.listdir(PPpath)
    title = []
    newNN = ''
    for i in file_n:
        if i.endswith("%s.txt" % nn):
            orgN = os.path.join(PPpath, i)
            title.append(i)
            for m in range(len(title)):
                title[m] = title[m].replace(nn, new)
                newN = os.path.join(PPpath, title[m])
            os.rename(orgN, newN)
            with open('%s' % i, 'r', encoding='UTF-8') as list:
                nnl = list.readlines()
                nnl[1] = '닉네임:%s\n' % new
                for m in nnl:
                    m.strip('\n')
                result = ''.join(map(str, nnl))
                newNN += result
                print(newNN)
            with open("%s" % i, 'w', encoding='UTF-8') as list:
                list.write(newNN)


    for i in file_n:
        if i.endswith("%s 댓글 목록.txt" % nn):
            orgN = os.path.join(PPpath, i)
            title.append(i)
            for m in range(len(title)):
                title[m] = title[m].replace(nn, new)
                newN = os.path.join(PPpath, title[m])
            os.rename(orgN, newN)

