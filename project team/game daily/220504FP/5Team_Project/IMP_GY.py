
import IMP_SH as SH

def U_IM_file(code):
    import os.path
    path1 = ("%sIMIP.txt" % code)
    path2 = ("%sIMOP.txt" % code)
    if os.path.isfile(path1) and os.path.isfile(path2):
        pass

    else:
        Title = {"물품고유코드": ["물품번호", "제품명", "센터", "섹터", "카테고리", "유통기한(S)", "유통기한(E)", "입고일", "출고일", "금액", "부피", "무게"]}
        y = SH.U_dicTostr(Title)
        IMIP = open("%sIMIP.txt" % code, 'w', encoding="UTF-8")
        IMIP.write(str(y))
        IMIP.close()
        IMOP = open("%sIMOP.txt" % code, 'w', encoding="UTF-8")
        IMOP.write(str(y))
        IMOP.close()

def U_CI_file(code, name, adress,Vmax,Smax):
    import os.path
    path="%s.txt" %code

    if os.path.isfile(path) :
        pass

    else :
        xx = {"코드명": ["지역", "주소", "최대적재부피", "섹터별부피"]}
        xx[code]=[name, adress, Vmax, Smax]
        x=SH.U_dicTostr(xx)
        info_file=open("%sINFO_F.txt" % code, 'w', encoding="UTF-8")
        info_file.write(str(x))
        info_file.close()

def Pro_code():  # 물품고유코드 (딕셔너리 키값)
    import random
    al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z''1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    aa = random.sample(al, 8)
    h = ""
    for m in aa:
        h += m
    import datetime
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    y = (date.split("-")[0])
    yy = y[2:]
    m = (date.split("-")[1])
    mm = m
    yymm = yy + mm
    code = yymm + h
    return code


# def Product_in():
#     Name = "머슬핏상의" #p_f1_1ent1.get()  # 상품명  UI에서 가져오는 값이라 안되는거 임의로 변수 선언해서 돌려보기
#     Cate = "남성패션" #p_f1_1ent2.get()  # 카테고리(남성패션 등)
#     Price = 32000 #p_f1_1ent3.get()  # 가격
#     Volume = 1 #p_f1_1ent4.get()  # 부피
#     KG = 1 #p_f1_1ent5.get()  # 무게
#     AA = [Name, Cate, Price, Volume, KG]  # 위 리스트
#
#     if "" not in AA:
#         import os.path
#         path = '0_IP_List.txt'
#         if os.path.isfile(path):
#             Namelist = SH.U_strTodic('0_IP_List')
#             a=list(Namelist.values())
#             print(a)
#             aa=a[-1][0] #제품번호
#             print(aa)
#             aaa=aa[-1].isdigit() #숫자포함 여부
#             if aaa :
#                 if Name not in Namelist:
#                     x = SH.catelist()
#                     if Cate in x:
#                         X = SH.U_strTodic('0_IP_list')
#                         X_1 = list(X.values())
#                         X_2 = []
#                         for i in X_1[1:]:
#                             X_2.append(i[0])
#                         X_3 = X_2[-1]
#                         X_4 = X_3.split("-")
#                         X_5 = ""
#
#                         P_num_A = ""
#                         for i in range(len(category1)): #카테고리로 섹터찾기
#                             if Cate in category1[i]:
#                                 P_num_A += category2[i]
#                             else:
#                                 pass
#
#                         if 9999 == int(X_4[3]):
#
#                             A = int(X_4[1]) + 1
#                             X_5 += P_num_A
#                             X_5 += "-"
#                             X_5 += str(A)
#                             X_5 += "-"
#                             X_5 += X_4[2]
#                             X_5 += "-"
#                             X_5 += '1001'
#
#                         else:
#                             A = int(X_4[3]) + 1
#                             X_5 += P_num_A
#                             X_5 += "-"
#                             X_5 += X_4[1]
#                             X_5 += "-"
#                             X_5 += X_4[2]
#                             X_5 += "-"
#                             X_5 += str(A)
#
#                         X_6 = [X_5, Cate, Price, Volume, KG]
#                         X_7 = {}
#                         X_7[Name] = X_6
#                         X_8 = SH.U_dicTostr(X_7)
#
#                         file = open("0_IP_List.txt", "a", encoding="UTF-8")
#                         file.write(X_8)
#                         file.close()
#
#                         # tk.messagebox.showinfo('알림', '상품등록을 완료하였습니다.')
#                         # product.tkraise()
#
#                     else:
#                         print("카테고리x")
#                         # tk.messagebox.showerror('알림', '카테고리가 존재 하지 않음.')
#                         # product.tkraise()
#                 else:
#                     print("기존상품, 이름있음 ")
#                     # tk.messagebox.showerror('알림', '같은상품이 존재함.')
#                     # product.tkraise()
#             else:
#                 title = {'상품명': ['제품번호', '카테고리', '금액', '부피', '무게']}
#                 P_num_A = ""
#                 for i in range(len(category1)):
#                     if Cate in category1[i]:
#                         P_num_A += category2[i]
#                     else:
#                         pass
#                 P_num_B = P_num_A + '-10-IMP-1001'
#                 P_num = [P_num_B, Cate, Price, Volume, KG]
#                 title[Name] = P_num
#
#                 title_A = SH.U_dicTostr(title)
#
#                 file = open("0_IP_List.txt", "w", encoding="UTF-8")
#                 file.write(title_A)
#                 file.close()
#
#         else:
#             title = {'상품명': ['제품번호', '카테고리', '금액', '부피', '무게']}
#             P_num_A = ""
#             for i in range(len(category1)):
#                 if Cate in category1[i]:
#                     P_num_A += category2[i]
#                 else:
#                     pass
#             P_num_B = P_num_A + '-10-IMP-1001'
#             P_num = [P_num_B, Cate, Price, Volume, KG]
#             title[Name] = P_num
#
#             title_A = SH.U_dicTostr(title)
#
#             file = open("0_IP_List.txt", "w", encoding="UTF-8")
#             file.write(title_A)
#             file.close()
#
#                     # tk.messagebox.showinfo('알림', '상품등록을 완료하였습니다.')
#                     # product.tkraise()
#     else:
#         pass
#             # tk.messagebox.showerror('알림', '공백이 존재할 수 없습니다.')
#             # product.tkraise()
