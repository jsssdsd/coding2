# like 여부 체크하기
def checkLike(user,postClass):
    file=open('like.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines=lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
        if postClass.postNum == lines[i][0] and user.id == lines[i][1]:
            return
    return 'not yet'
# like 하기
def likeowYou(user,postClass):
    file=open('like.txt','a',encoding='UTF-8')
    file.write('{}\t{}\t{}\n'.format(postClass.postNum,user.id,user.n_name))
    file.close()
# unlike 하기
def unlikeYou(user,postClass):
    file=open('like.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines.remove('{}\t{}\t{}\n'.format(postClass.postNum,user.id,user.n_name))
    file=open('like.txt','w',encoding='UTF-8')
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()
# 해당 게시물 좋아요수 리턴
def cntLike(postClass):
    file=open('like.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines=lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    cnt2=0
    for i in range(len(lines)):
        if  lines[i][0]==postClass.postNum:
            cnt2+=1
    return cnt2
# like 수 판별하기
# (기준 일, 좋아요 상위 몇 개)
# 인덱싱 가능한 형태로 리턴 튜플 혹은 리스트
def likeCount(day,num):
    import time
    day0=int(day)*86400 # '기준' 날짜를 초로 변환
    day1=time.time() # '지금' 시간을 초로 표현
    file=open('post.txt','r',encoding='UTF-8')
    post=file.readlines()
    file.close()
    post=post[1:]
    posting=[]
    for i in range(len(post)):
        post[i]=post[i].strip().split('\t')
    # 기준일에 해당하는 게시물 쌓기
    for i in range(len(post)):
        if day1 - float(post[i][3]) <= day0 :
            posting.append(post[i])
    # 좋아요 전처리
    file=open('like.txt','r',encoding='UTF-8')
    like=file.readlines()
    file.close()
    like=like[1:]
    for i in range(len(like)):
        like[i]=like[i].strip().split('\t')

    # 좋아요수 세기
    # lines0
    # lines1 은 좋아요 전처리
    temp_1=[]
    temp_2=[]
    for i in range(len(like)):
        temp_2.append(like[i][0])
    for i in range(len(posting)):
        cnt2=temp_2.count(posting[i][0])
        temp_1.append([posting[i],cnt2])
    temp_list=sorted(temp_1, key=lambda  like: like[1], reverse=True)
    if len(temp_list) > num:
        temp_list=temp_list[:num]
    else:
        pass
    return temp_list