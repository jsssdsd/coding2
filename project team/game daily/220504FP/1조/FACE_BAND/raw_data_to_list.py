# def followingData (a,b):
#     lines=follow()
#     for i in range(len(lines)):
#         if a in lines[i][0]:
#             if b in lines[i][1]:
#                 return print('이미 팔로우 중 입니다.')
#     file=open('following.txt','a',encoding='UTF-8')
#     file.write('{}\t{}\n'.format(a,b))
#     file.close()
#
# def unfollowingData (a,b):
#     lines=follow()
#     print(lines)
#     for i in range(len(lines)):
#         if a in lines[i][0]:
#             if b in lines[i][1]:
#                 lines.remove(lines[i])
#     print(lines)
#     file=open('following.txt','w',encoding='UTF-8')
#     for i in range(len(lines)):
#         file.write('{}\t{}\n'.format(lines[i][0],lines[i][1]))
#
# # def check_cross(id1,id2):

def userData ():
    file = open('user.txt','r',encoding='UTF-8')
    lines = file.readlines()
    file.close()
    lines = lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    return lines

def postData ():
    file = open('post.txt','r',encoding='UTF-8')
    lines = file.readlines()
    file.close()
    lines = lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    return lines

def likeData():
    file=open('like.txt','r',encoding='UTF-8')
    lines = file.readlines()
    file.close()
    lines=lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    return lines

def commentData():
    file=open('comment.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines=lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    return lines

def followData ():
    file = open('following.txt','r',encoding='UTF-8')
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    return  lines

#

