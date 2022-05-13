import time
class post:
    def __init__(self,detail,ID,time,secret,NICK):
        self.detail=detail
        self.ID=ID
        self.time=time
        self.secret=secret
        self.NICK = NICK

def checklist() : # 파일의 여부 확인 및 생성
    import os.path
    path = "post.txt"
    if os.path.isfile(path) :
        pass
    else :
        x="post_num\tID\t내용\t시간\t비밀글여부\n"
        list=open("post.txt", "w", encoding="UTF-8")
        list.write(x)
        list.close()
    path = 'cnt.txt'
    if os.path.isfile(path):
        pass
    else:
        list=open('cnt.txt','w',encoding='UTF-8')
        list.write('1')
        list.close()

def list_write(user_write): # 파일에 데이터 추가
    file=open('cnt.txt','r',encoding='UTF-8')
    cnt=file.readline()
    file.close()
    cnt=int(cnt)
    a = open("post.txt", "a", encoding="UTF-8")
    a.write("%s\t%s\t%s\t%s\t%s\t%s\n" % ('po_{}'.format(cnt),user_write.ID, user_write.detail, user_write.time, user_write.secret, user_write.NICK))
    a.close()
    cnt+=1
    file=open('cnt.txt','w',encoding='UTF-8')
    file.write(str(cnt))
    file.close()

def pt(userID,content,secret,NICK):
    import time
    time = time.time()
    user_write=post(content, userID, time, secret,NICK)
    list_write(user_write)

if __name__=="__main__": # 실행 예
    print('포스팅모듈')