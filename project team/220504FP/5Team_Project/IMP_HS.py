import IMP_SH as SH


SU = "서울"
DJ = "대전"
GJ = "광주"
DG = "대구"
BS = "부산"

FS=["남성패션", "여성패션", "공용패션", "패션기타"]
AC=['모자', '가방', '신발', '기타악세서리']
BT=['스킨케어', '클렌징', '메이크업', '헤어제품', '뷰티기타']
KC=['조리도구', '냄비/프라이팬', '칼/도마', '기타주방']
DN=['화장지/물티슈', '샤워용품', '욕실청소', '화장실청소', '일회용품', '생필품기타']
Title = {"물품고유코드": ["물품번호", "제품명", "센터", "카테고리", "유통기한(시작일)", "유통기한(마감일)", "입고일", "출고일","금액", "부피", "무게" ]}

c=["SU","DJ","GJ","DG","BS"]
cc=[FS,AC,BT,KC,DN]
ccc=[SU,DJ,GJ,DG,BS]




# U_OP()
#  - 출고 기능
#  - 인풋으로 출고일자를 받는다.
#  - 출고되는 제품은 입고일 기준 가장 빠른 데이터를 순차적으로 출고 처리 한다.
#  - 출고시에는 출고일자를 입력한뒤, 출고파일에 데이터를 누적 시키고
#  - 입고 파일에서는 기존 출고데이터를 삭제 처리 한다.


def U_OP():


    center_selete=""   #########################  센터 입력  #########################
    product_name=""   ##########################  제품명 입력  #########################
    product_int=int(0)   ##########################  제품 갯수 입력  #########################


    entire_list=[]  #  선택한 센터(center_selete) , 제품(product_name) 에 해당하는 물품을 담아주는 리스트
    sort_list=[]  #  entire_list에 저장된 리스트를 입고일 우선 기준, 제품갯수(product_int) 만큼 담아주는 리스트
    sort_dic = {}  #  sort_list에 저장된 리스트에서 물품고유코드를 키값, 나머지를 밸류값에 넣어주는 딕셔너리
    cr = []  #  c 리스트에서 센터(center_selete) 를 뺀 리스트

    print('='*100)  # 구분하는 선
    print("선택하신 출고 데이터 최종 확인")
    print("센터:%s  제품명:%s  수량:%s개"%(center_selete,product_name,product_int))
    print('='*100)  # 구분하는 선
    print("선택하신 제품이 맞습니까?")


    YN = "Y"   #########################  입력한 제품이 맞는지 결정  #########################  ( 출고 데이터 최종 확인 )


    print('='*100) #  구분하는 선

    if center_selete in c and YN in ("예","Y","y","YES","yes","Yes","네"):   #####  c 리스트 안에 선택한 센터(center_selete) 가 있으면, 입력한 제품이 맞으면  ( 센터 재고 조회 )
        dd=SH.U_strTolist("%sIMIP"%center_selete)  #  선택한 센터의 파일을 리스트 시킴
        for IP_list in dd:  #  리스트 시킨 파일을 for 문 돌림
            if product_name==IP_list[2]:  #  선택한 제품이랑 for 문 돌린 리스트 안의 제품명(product_name) 이 같은지 확인
                import time as t
                if IP_list[7]=="-" or IP_list[7]>=t.strftime('%y-%m-%d', t.localtime()):
                    entire_list.append(IP_list)  #  제품명이 같은 리스트를 entire_list에 저장

        if len(entire_list)>=product_int and product_int>0:   #####  제품명이 같은 리스트(entire_list) 의 갯수가 선택한 갯수(product_int) 보다 크거나 같으면, 그리고 선택한 갯수(product_int) 가 0보다 크면  (재고 수량 가능)
            print("%s센터 %s 재고 총 %d개"%(center_selete,product_name,len(entire_list)))
            print("선택하신 수량 %s개"%product_int)
            print("재고 수량 가능")
            print('='*100) #구분하는 선

            entire_list.sort(key=lambda x: x[8])   #####  제품명이 같은 리스트(entire_list) 중에서 입고일이 제일 빠른 항목을 우선 순위대로 나열  ( 입고일 우선 정렬 )
            for PI in range(product_int):  #  선택한 갯수(product_int) 를 for 문으로 슬라이싱하여 PI에 저장
                sort_list.append(entire_list[PI])  #  제품명이 같은 리스트(sort_list) 중에서 선택한 갯수(product_int) 를 슬라이싱하여 해당 되는 리스트를 sort_list 리스트에 저장

            for SD in range(len(sort_list)):  #  제품명이 같고 선택한 갯수만 넣은 리스트(sort_list) 의 갯수를 슬라이싱하여 SD 에 저장
                import time as t  #  time 모듈 호출
                sort_list[SD][9] = t.strftime('%y-%m-%d', t.localtime())  #  제품명이 같고 선택한 갯수만 넣은 리스트(sort_list) 들의 출고일을 오늘 날짜로 바꿔줌
                sort_dic[sort_list[SD][0]] = sort_list[SD][1:]  #  제품명이 같고 선택한 갯수만 넣은 리스트(sort_list) 의 물품고유코드를 키값, 나머지를 밸류값에 저장

            IPstrSD = SH.U_dicTostr(sort_dic)  #  sort_dic 딕셔너리를 문자열로 바꿔서 IPstrSD 에 저장

            OPFile2 = open("%sIMOP.txt" % center_selete, 'a', encoding='UTF-8')   #####  선택한 센터(center_Selete) 출고 파일의 맨 밑에  ( 출고 데이터 생성 저장 )
            OPFile2.write(IPstrSD)  #  문자열(IPstrSD) 을 저장
            OPFile2.close()  #  파일을 닫음

            for SDK in sort_dic.keys():   #####  sort_dic의 키 값을 for 문으로 돌려서 SDK에 저장  ( 입고 데이터 삭제 저장)
                import fileinput  #  fileinput 모듈 호출
                import sys  #  sys 모듈 호출
                for line in fileinput.input('%sIMIP.txt' % center_selete, inplace=True, encoding='UTF-8'):  #  fileinput.input 으로 선택한 센터 출고 파일을 열어서 읽고 지워줌. for 문으로 line에 저장
                    if SDK in line:  #  line 안에 sort_dic의 키 값(SDK) 이 들어가 있다면
                        line = line.replace(line, '')  #  line 문장을 ''(공백) 으로 변경함
                    sys.stdout.write(line)  #  inplace=True 로 인해 지워진 문장들을 다시 적어줌

            print("출고 완료")
            print('=' * 100)  # 구분하는 선
            print("%s 센터 %s 재고 남은 수량 %d개" % (center_selete, product_name, int(len(entire_list))-product_int))

        elif len(entire_list)<product_int and product_int>0:   #####  제품명이 같은 리스트(entire_list) 의 갯수가 선택한 갯수(product_int) 보다 작다면, 그리고 선택한 갯수(product_int) 가 0보다 크면  ( 재고 수량 불가능 )
            print("%s센터 %s 재고 총 %d개" % (center_selete, product_name, len(entire_list)))
            print("선택하신 수량 %s개" % product_int)
            print("재고 수량 불가능")
            print('=' * 100) # 구분하는 선
            print("타 센터 동일 제품 재고 조회")

            for CC in c:  #  c 리스트를 for 문을 돌려서 CC에 저장
                cr.append(CC)  #  for 문 돌린 CC를 cr리스트에 저장
            cen_index=cr.index(center_selete)  #  선택한 센터(center_selete) 가 cr 리스트의 몇 번째에 있는지 인덱싱을 돌려서 cen_index 에 저장
            cr.remove(center_selete)  #  cr 리스트 안에서 선택한 센터(center_selete)를 지워줌
            for CR in cr:  #  선택한 센터(center_selete)를 지운 cr 리스트를 for 문을 돌려서 CR 에 저장

                mul_list = []  #  선택한 제품명(product_name)에 해당되는 품목이 저장되어 있는 리스트

                tt=SH.U_strTolist("%sIMIP"%CR)   #####  CR 에 해당되는 입고파일을 리스트화 시켜서 tt 에 저장  ( 타 센터 동일 제품 재고 조회 )
                for ttIP_list in tt:  #  리스트화 시킨 tt 를 for 문을 돌려서 ttIP_list 에 저장
                    if product_name == ttIP_list[2]:  #  ttIP_list 의 제품명이 선택한 제품명(product_name)이랑 같으면
                        import time as t
                        if ttIP_list[7] == "-" or ttIP_list[7] >= t.strftime('%y-%m-%d', t.localtime()):
                            mul_list.append(ttIP_list)  #  ttIP_list 를 mul_list에 저장

                print('=' * 100)  # 구분하는 선
                print("%s 센터 %s 재고 수량 %d개" % (CR, product_name, len(mul_list)))
                print("선택하신 수량 %s개" % product_int)

                if len(mul_list)>=product_int:   #####  mul_list 리스트 안의 갯수가 선택한 갯수(product_int) 보다 크거나 같으면  ( 타 센터 재고 수량 확인 )
                    print("수량 가능")
                elif len(mul_list)<product_int:  #  mul_list 리스트 안의 갯수가 선택한 갯수(product_int) 보다 작으면
                    print("수량 안됨")


                tacenter_selete = ""   #########################  출고시킬 타 센터 선택 ( 출고 시킬 타 센터 선택 )  #########################


                if tacenter_selete==CR and len(mul_list)>=product_int:   #####  출고시킬 타 센터(tacenter_selete) 가 CR이랑 같으면, 그리고 mul_list 리스트 안의 갯수가 선택한 갯수(product_int) 보다 크거나 같으면
                    print('=' * 100)  # 구분하는 선
                    print("%s 센터 출고 가능"%CR)

                    mul_list.sort(key=lambda x: x[8])   #####  mul_list(선택한 제품(product_name) 이 들어있는 리스트) 의 입고일 항목을 제일 빠른 순으로 정렬

                    for PI in range(product_int):  #  선택한 갯수(product_int) 를 슬라이싱 시켜서 PI 에 저장
                        sort_list.append(mul_list[PI])  #  mul_list(선택한 제품(product_name) 이 들어있는 리스트) 의 품목을 PI 의 갯수 만큼만 sort_list 리스트에 저장
                    for SD in range(len(sort_list)):  #  sort_list(선택한 갯수(product_int) 만큼만 저장한 리스트) 안의 항목을 for 문을 돌려서 슬라이싱 시켜서 SD 에 저장
                        sort_list[SD][3]=ccc[cen_index]  #  sort_list(선택한 갯수(product_int) 만큼만 저장한 리스트) 의 센터 이름을, ccc 리스트의 cen_index 번째로 변경
                        sort_dic[sort_list[SD][0]] = sort_list[SD][1:]  #  sort_list 의 물품고유코드를 키값, 나머지를 밸류값에 저장

                    IPstrSD = SH.U_dicTostr(sort_dic)  #  sort_dic 딕셔너리를 문자열로 바꿔서 IPstrSD 에 저장

                    OPFile2 = open("%sIMIP.txt" % center_selete, 'a', encoding='UTF-8')   #####  선택한 센터(center_Selete) 입고 파일의 맨 밑에  ( 타 센터 재고를, 우리 센터의 입고 파일로 저장 )
                    OPFile2.write(IPstrSD)  #  문자열(IPstrSD) 을 저장
                    OPFile2.close()  #  파일을 닫음

                    for SDK in sort_dic.keys():   #####  sort_dic의 키 값을 for 문으로 돌려서 SDK에 저장 ( 타 센터의 입고 데이터 삭제 저장 )
                        import fileinput  #  fileinput 모듈 호출
                        import sys  #  sys 모듈 호출
                        for line in fileinput.input('%sIMIP.txt' % CR, inplace=True, encoding='UTF-8'):    #  fileinput.input 으로 CR 센터 입고 파일을 열어서 읽고 지워줌. for 문으로 line에 저장
                            if SDK in line:  #  line 안에 sort_dic의 키 값(SDK) 이 들어가 있다면
                                line = line.replace(line, '')  #  line 문장을 ''(공백) 으로 변경함
                            sys.stdout.write(line)  #  inplace=True 로 인해 지워진 문장들을 다시 적어줌

                    for SD in range(len(sort_list)):  #  제품명이 같고 선택한 갯수만 넣은 리스트(sort_list) 의 갯수를 슬라이싱하여 SD 에 저장
                        import time as t  #  time 모듈 호출
                        sort_list[SD][9] = t.strftime('%y-%m-%d', t.localtime())  #  제품명이 같고 선택한 갯수만 넣은 리스트(sort_list) 들의 출고일을 오늘 날짜로 바꿔줌
                        sort_dic[sort_list[SD][0]] = sort_list[SD][1:]    #  제품명이 같고 선택한 갯수만 넣은 리스트(sort_list) 의 물품고유코드를 키값, 나머지를 밸류값에 저장

                    IPstrSD = SH.U_dicTostr(sort_dic)  # sort_dic 딕셔너리를 문자열로 바꿔서 IPstrSD 에 저장

                    OPFile2 = open("%sIMOP.txt" % center_selete, 'a',encoding='UTF-8')   ##### 선택한 센터(center_Selete) 출고 파일의 맨 밑에 ( 출고 데이터 생성 저장 )
                    OPFile2.write(IPstrSD)  # 문자열(IPstrSD) 을 저장
                    OPFile2.close()  # 파일을 닫음

                    for SDK in sort_dic.keys():   #####  sort_dic의 키 값을 for 문으로 돌려서 SDK에 저장 ( 입고 데이터 삭제 저장)
                        import fileinput  # fileinput 모듈 호출
                        import sys  # sys 모듈 호출
                        for line in fileinput.input('%sIMIP.txt' % center_selete, inplace=True, encoding='UTF-8'):
                            if SDK in line:  # line 안에 sort_dic의 키 값(SDK) 이 들어가 있다면
                                line = line.replace(line, '')  # line 문장을 ''(공백) 으로 변경함
                            sys.stdout.write(line)  # inplace=True 로 인해 지워진 문장들을 다시 적어줌

                    print('=' * 100)  # 구분하는 선
                    print("출고 완료")
                    print("%s 센터 %s 재고 남은 수량 %d개" % (tacenter_selete, product_name, int(len(mul_list))-product_int))
                    break

                elif tacenter_selete==CR and len(mul_list)<product_int:  #  출고시킬 타 센터(tacenter_selete) 가 CR이랑 같으면, 그리고 mul_list 리스트 안의 갯수가 선택한 갯수(product_int) 보다 작다면
                    print('=' * 100)  # 구분하는 선
                    print("%s 센터 선택"%CR)
                    print("%s 센터 수량 부족"%CR)
                    break

        elif product_int<=0:  #  선택한 갯수(product_int) 가 0보다 작거나 같으면
            print("수량을 잘못 입력 하셨습니다.")
            print("처음으로 돌아갑니다.")

    elif center_selete not in c:  #  c 리스트 안에 선택한 센터(center_selete) 가 있지 않으면
        print("센터명을 잘못 입력 하셨습니다.")
        print("처음으로 돌아갑니다.")

    elif YN not in ("예", "Y", "y", "YES", "yes", "Yes", "네"):  # 선택한 제품이 아니라면
        print("선택하신 제품이 아닙니다.")
        print("처음으로 돌아갑니다.")

    else:
        print("처음으로 돌아갑니다.")



'''
        with open("%sIMIP.txt"%center_selete,"r",encoding='UTF-8') as f:
            lines = f.readlines()
        with open("%sIMIP.txt"%center_selete,"w",encoding='UTF-8') as f:
            for line in lines:
                if line.strip("\n") !=OPstrSD2 :  # <= 이 문자열만 골라서 삭제
                    f.write(line)
        '''


# U_IP_Check()
#  - 재고현황 조회 기능
#  - 조회하고자 하는 센터 와 카테고리를 받음
#  - 받은 값에 해당하는 파일을 불러옴
#  - 불러온데이터를 가공
#  - 물품번호를 카운트하여 해당재품이 몇개씩 있는지 약식 노출 한다.
#    ex. AAAA 상품 154개
#  - 필요에따라 전체 리스트를 보여준다
#
# * 센터 전체 리스트, 카테고리 전체리스트, 센터별리스트 등을 표현할 수 있어야 한다.
#  - 부분만 되어선 안됨


def U_IP_Check():


    center_selete = ""   #########################  센터 선택 예) "전체" , "SU"  #########################
    category_selete = ""   #########################  카테고리 선택 예) BT[3] , DN[4]  #########################


    entire_list = []  #  선택한 센터(center_selete) 의 품목들을 저장하는 리스트

    for i in range(len(cc)):  #  cc 리스트 안의 갯수를 슬라이싱 시켜서 i 에 저장
        if center_selete in c and category_selete in cc[i]:  #  c 리스트 안에 선택한 센터(center_selete)가 있다면, 그리고 선택한 카테고리(category_selete) 가 cc 의 i 번째 안에 들어간다면
            dd=SH.U_strTolist("%sIMIP"%center_selete)  #  선택한 센터(center_selete) 에 해당되는 입고 파일을 리스트화 시키고 dd 에 저장함
            for IP_list in dd:  #  dd 를 for 문 돌려서 IP_list 에 저장
                if category_selete in IP_list:  #  선택한 센터(center_selete) 에 해당되는 리스트(IP_list) 안에 선택한 카테고리(category_selete) 가 들어가 있다면
                    entire_list.append(IP_list)  #  IP_list 를 entire_list 에 저장


    if center_selete in c and category_selete == "전체":  #  c 리스트 안에 선택한 센터(center_selete)가 있다면, 그리고 선택한 카테고리(category_selete)가 "전체" 와 같다면
        dd=SH.U_strTolist("%sIMIP"%center_selete)  #  선택한 센터(center_selete) 에 해당되는 입고 파일을 리스트화 시키고 dd 에 저장함
        for list_Dead in dd:  #  dd 를 for 문 돌려서 list_Dead 에 저장
            entire_list.append(list_Dead)  #  list_Dead 를 entire_list 에 저장

    elif center_selete == "전체":  #  선택한 센터(center_selete) 가 "전체"와 같다면
        for i in c:  #  c 리스트를 for 문 돌려서 i 에 저장
            dd = SH.U_strTolist("%sIMIP" % i)  #  선택한 센터(center_selete) 에 해당되는 입고 파일을 리스트화 시키고 dd 에 저장함
            for i in range(len(cc)):  #  cc 리스트의 갯수를 슬라이싱 시켜서 i 에 저장
                if category_selete in cc[i]:  #  선택한 카테고리(category_selete) 가 cc 의 i 번째 안에 들어간다면
                    for IP_list in dd:  #  dd 를 for 문 돌려서 IP_list에 저장
                        if category_selete in IP_list:  #  선택한 센터(center_selete) 에 해당되는 리스트(IP_list) 안에 선택한 카테고리(category_selete) 가 들어가 있다면
                            entire_list.append(IP_list)  #  IP_list 를 entire_list 에 저장
            if category_selete == "전체":  #  선택한 카테고리(category_selete) 가 "전체"와 같다면
                for list_dead in dd:  # dd 를 for 문 돌려서 list_dead 에 저장
                    entire_list.append(list_dead)  # list_dead 를 entire_list 에 저장


    print_selete = ""   #########################  기능 넣는 곳 예) "AP" , "FP"  #########################


    if print_selete=="AP":  #  약식 출력

        print("약식 출력")
        print("%s %d개 보유"%(category_selete,len(entire_list)))

    elif print_selete=="FP":  #  전체 출력

        print("전체 출력")
        for FP_gagong in entire_list:  #  전체 리스트(entire_list) 를 for 문 돌려서 FP_gagong 에 저장
            print(FP_gagong)


    elif print_selete=="IP":  #  입고일 선택 출력


        IPday = ""   #########################  입고일 선택 예) "22-04-22" , "22-04-25"   #########################


        IPday_list = []  #  선택한 입고일(IPday) 에 해당하는 품목이 들어가 있는 리스트
        print("입고일: %s일자 목록" % IPday)
        for entire_list2 in entire_list:  #  entire_list 를 for 문 돌려서 entire_list2 에 저장
            if IPday in entire_list2[8] :  #  입고일(entire_list2[7]) 안에 선택한 입고일(IPday) 이 들어가면
                IPday_list.append(entire_list2)  #  IPday_list2 를 IPday_list 안에 저장
        for ipi in IPday_list:  #  IPday_list 를 for 문 돌려서 ipi 에 저장
            print(ipi)


    elif print_selete=="PP":  #  상품명 검색 출력


        PPday = ""  #########################  상품명 입력 예) 나무젓가락, 드라이기  #########################

        PPday_list = []  #  선택한 상품명(PPday) 에 해당하는 상품이 들어가 있는 리스트
        for entire_list2 in entire_list:  #  전체 리스트(entire_list) 를 for 문 돌려서 entire_list2에 저장
            if PPday in entire_list2[2]:  #  상품명(entire_list2[2]) 안에 선택한 상품(PPday) 이 들어가면
                PPday_list.append(entire_list2)  #  OPday_list2 를 PPday_list 안에 저장

        if PPday_list == []:  #  PPday_list 가 비어있으면
            print("%s센터 %s카테고리 안에 %s을 찾을 수 없습니다." % (center_selete, category_selete, PPday))
        else:
            print("%s 목록" % PPday)
        for ppi in PPday_list:  #  PPday_list 를 for 문 돌려서 ipi 에 저장
            print(ppi)


    elif print_selete == "EXS":  #  유통기한(시작일) 검색 출력


        EXSday = ""  #  #########################  유통기한(시작일) 입력 예) "22-04-22" , "22-04-25" , 유통기한이 없으면 - 입력  #########################


        EXSday_list = []  # 선택한 유통기한(시작일)(EXSday) 에 해당하는 품목이 들어가 있는 리스트
        print("유통기한(시작일): %s일자 목록" % EXSday)
        for entire_list2 in entire_list:  # entire_list 를 for 문 돌려서 entire_list2 에 저장
            if EXSday in entire_list2[6]:  # 유통기한(시작일)(entire_list2[5]) 안에 선택한 유통기한(시작일)(EXSday) 이 들어가면
                EXSday_list.append(entire_list2)  # IPday_list2 를 EXSday_list 안에 저장
        for exsi in EXSday_list:  # EXSday_list 를 for 문 돌려서 exsi 에 저장
            print(exsi)


    elif print_selete == "EXE":  #  유통기한(마감일) 검색 출력


        EXEday = ""  #  #########################  유통기한(마감일) 입력 예) "22-04-22" , "22-04-25" , 유통기한이 없으면 - 입력  #########################


        EXEday_list = []  # 선택한 유통기한(마감일)(EXSday) 에 해당하는 품목이 들어가 있는 리스트
        print("유통기한(마감일): %s일자 목록" % EXEday)
        for entire_list2 in entire_list:  # entire_list 를 for 문 돌려서 entire_list2 에 저장
            if EXEday in entire_list2[7]:  # 유통기한(마감일)(entire_list2[6]) 안에 선택한 유통기한(마감일)(EXEday) 이 들어가면
                EXEday_list.append(entire_list2)  # IPday_list2 를 EXEday_list 안에 저장
        for exei in EXEday_list:  # EXEday_list 를 for 문 돌려서 exei 에 저장
            print(exei)




# U_OP_Check()
#  - 출고현황 조회 기능
#  - 전체 물류상태에서 어떤 물건이 몇개 출고(판매처리) 가 되었는지 조회 한다.
#
#  - 전체가 아닌 부분 데이터 확인이 가능해야함
#    ex. 서울센터, 대전센터 따로 조회
#
#  - 출고일을 기준으로 조회 할 수도 있어야 한다.


def U_OP_Check():


    center_selete = ""   ######################### 센터 선택 예) "전체" , "SU"  #########################
    category_selete = ""   #########################  카테고리 선택 예) BT[3] , DN[4]  #########################


    entire_list = []  #  선택한 센터(center_selete) 의 품목들을 저장하는 리스트

    for i in range(len(cc)):  #  cc 리스트 안의 갯수를 슬라이싱 시켜서 i 에 저장
        if center_selete in c and category_selete in cc[i]:  #  c 리스트 안에 선택한 센터(center_selete)가 있다면, 그리고 선택한 카테고리(category_selete) 가 cc 의 i 번째 안에 들어간다면
            dd=SH.U_strTolist("%sIMOP"%center_selete)  #  선택한 센터(center_selete) 에 해당되는 출고 파일을 리스트화 시키고 dd 에 저장함
            for IP_list in dd:  #  dd 를 for 문 돌려서 IP_list에 저장
                if category_selete in IP_list:  #  선택한 센터(center_selete) 에 해당되는 리스트(IP_list) 안에 선택한 카테고리(category_selete) 가 들어가 있다면
                    entire_list.append(IP_list)  #  IP_list 를 entire_list 에 저장

    if center_selete in c and category_selete == "전체":  # c 리스트 안에 선택한 센터(center_selete)가 있다면, 그리고 선택한 카테고리(category_selete)가 "전체" 와 같다면
        dd = SH.U_strTolist("%sIMOP" % center_selete)  # 선택한 센터(center_selete) 에 해당되는 출고 파일을 리스트화 시키고 dd 에 저장함
        for list_Dead in dd:  # dd 를 for 문 돌려서 list_Dead 에 저장
            entire_list.append(list_Dead)  # list_Dead 를 entire_list 에 저장

    elif center_selete == "전체":  #  선택한 센터(center_selete) 가 "전체"와 같다면
        for i in c:  #  c 리스트를 for 문 돌려서 i 에 저장
            dd = SH.U_strTolist("%sIMOP" % i)  #  선택한 센터(center_selete) 에 해당되는 출고 파일을 리스트화 시키고 dd 에 저장함
            for i in range(len(cc)):  #  cc 리스트의 갯수를 슬라이싱 시켜서 i 에 저장
                if category_selete in cc[i]:  #  선택한 카테고리(category_selete) 가 cc 의 i 번째 안에 들어간다면
                    for IP_list in dd:  #  dd 를 for 문 돌려서 IP_list에 저장
                        if category_selete in IP_list:  #  선택한 센터(center_selete) 에 해당되는 리스트(IP_list) 안에 선택한 카테고리(category_selete) 가 들어가 있다면
                            entire_list.append(IP_list)  #  IP_list 를 entire_list 에 저장
            if category_selete == "전체":  #  선택한 카테고리(category_selete) 가 "전체"와 같다면
                for list_dead in dd:  # dd 를 for 문 돌려서 list_dead 에 저장
                    entire_list.append(list_dead)  # list_dead 를 entire_list 에 저장


    print_selete = ""   #########################  기능 넣는 곳 예) "AP" , "FP"  #########################


    if print_selete == "AP":  # 약식 출력

        print("약식 출력")
        print("%s %d개 보유" % (category_selete, len(entire_list)))


    elif print_selete == "FP":  #  전체 출력

        print("전체 출력")
        for FP_gagong in entire_list:  #  전체 리스트(entire_list) 를 for 문 돌려서 FP_gagong 에 저장
            print(FP_gagong)


    elif print_selete == "OP":  #  출고일 선택 출력


        OPday = ""  #########################  출고일 선택 예) "22-04-22" , "22-04-25"  #########################


        OPday_list = []  #  선택한 출고일(OPday) 에 해당하는 품목이 들어가 있는 리스트
        print("%s 센터" % center_selete)
        print("입고일: %s일자 목록" % OPday)
        for entire_list2 in entire_list:  #  entire_list 를 for 문 돌려서 entire_list2 에 저장
            if OPday in entire_list2[9]:  #  출고일(entire_list2[7]) 안에 선택한 출고일(OPday) 이 들어가면
                OPday_list.append(entire_list2)  #  OPday_list2 를 OPday_list 안에 저장
        for ipi in OPday_list:  #  OPday_list 를 for 문 돌려서 ipi 에 저장
            print(ipi)


    elif print_selete == "PP":  #  상품명 검색 출력


        PPday = ""   #########################  상품명 입력 예) 나무젓가락, 드라이기  #########################


        PPday_list = []  #  선택한 상품명(PPday) 에 해당하는 상품이 들어가 있는 리스트
        for entire_list2 in entire_list:  #  전체 리스트(entire_list) 를 for 문 돌려서 entire_list2에 저장
            if PPday in entire_list2[2]:  #  상품명(entire_list2[2]) 안에 선택한 상품(PPday) 이 들어가면
                PPday_list.append(entire_list2)  #  OPday_list2 를 PPday_list 안에 저장

        if PPday_list == []:  #  PPday_list 가 비어있으면
            print("%s센터 %s카테고리 안에 %s을 찾을 수 없습니다." % (center_selete, category_selete, PPday))
        else:
            print("%s 목록" % PPday)
        for ppi in PPday_list:  #  PPday_list 를 for 문 돌려서 ipi 에 저장
            print(ppi)


    elif print_selete == "EXS":  # 유통기한(시작일) 검색 출력


        EXSday = ""  # #########################  유통기한(시작일) 입력 예) "22-04-22" , "22-04-25" , 유통기한이 없으면 - 입력  #########################


        EXSday_list = []  # 선택한 유통기한(시작일)(EXSday) 에 해당하는 품목이 들어가 있는 리스트
        print("유통기한(시작일): %s일자 목록" % EXSday)
        for entire_list2 in entire_list:  # entire_list 를 for 문 돌려서 entire_list2 에 저장
            if EXSday in entire_list2[6]:  # 유통기한(시작일)(entire_list2[5]) 안에 선택한 유통기한(시작일)(EXSday) 이 들어가면
                EXSday_list.append(entire_list2)  # IPday_list2 를 EXSday_list 안에 저장
        for exsi in EXSday_list:  # EXSday_list 를 for 문 돌려서 exsi 에 저장
            print(exsi)


    elif print_selete == "EXE":  # 유통기한(마감일) 검색 출력


        EXEday = ""  # #########################  유통기한(마감일) 입력 예) "22-04-22" , "22-04-25" , 유통기한이 없으면 - 입력  #########################


        EXEday_list = []  # 선택한 유통기한(마감일)(EXSday) 에 해당하는 품목이 들어가 있는 리스트
        print("유통기한(마감일): %s일자 목록" % EXEday)
        for entire_list2 in entire_list:  # entire_list 를 for 문 돌려서 entire_list2 에 저장
            if EXEday in entire_list2[7]:  # 유통기한(마감일)(entire_list2[6]) 안에 선택한 유통기한(마감일)(EXEday) 이 들어가면
                EXEday_list.append(entire_list2)  # IPday_list2 를 EXEday_list 안에 저장
        for exei in EXEday_list:  # EXEday_list 를 for 문 돌려서 exei 에 저장
            print(exei)