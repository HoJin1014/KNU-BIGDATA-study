# === 나의 주소록 ===
# 1. 전체보기
# 2. 검 색
# 3. 추 가
# 4. 종 료

#def print_menu():
#    print("1. 전체보기")
#    print("2. 검 색")
#    print("3. 추 가")
#    print("4. 종 료")
#    menu= input("메뉴선택 : ")
#    return int(menu)

#def run():
#    while 1:
#        menu = print_menu()
#        if menu == 4:
#            break
#mmmmmmmmn

#friends = ["이호진, 01011112222, 대구, mk42987@naver.com", "홍길동, 01022223333, 서울, aaaaaa@naver.com", "베트맨, 01033334444, 경기도, nnnnnn@naver.com", "마마마, 01034344212, 인천, nngdgdn@naver.com", "아아아, 010323243314, 부산, fsfsnn@naver.com"]

#select = 0

#while select != 4:
#    print("--------------------------")
#    print("1. 전체보기")
#    print("2. 검 색")
#    print("3. 추 가")
#    print("4. 종 료")
#    select = int(input("메뉴를 선택하시오 : "))

#    if select == 1:
#        print(friends)

#    elif select == 2:
#        print(find())


       # del_name = input("검색할 이름을 입력하시오 : ")
       # if del_name in friends:
       #     friends.remove(del_name)
       #else:
       #     print("해당 이름이 존재하지 않습니다.")


 #   elif select == 3:
      #  friends.insert()



       # add_name = input("전화번호부를 입력하시오 : ")


#    elif select == 4:
       # print("전화번호부를 종료합니다.")

# 전화번호부 제목
#friend1='이호진 01011112222 대구.txt'
#file=open(friend1, 'w' , encoding='utf-8')
#file.write('이호진, 01011112222, 대구')
#file.close()

#friend2='홍길동 01022223333 서울.txt'
#file=open(friend2, 'w' , encoding='utf-8')
#file.write('홍길동, 01022223333, 서울')
#file.close()

#friend3='아아아 01055556666 경기도.txt'
#file=open(friend3, 'w' , encoding='utf-8')
#file.write('아아아, 01055556666, 경기도')
#file.close()

#list=[friend1,friend2,friend3]
#while True:
#    print("=============")
#    print("1.전체보기")
#    print("2.검 색")
#    print("3.추 가")
#    print("4.종 료")
#    print("==============")
#    myNum=input("메뉴 선택: ")
#    if myNum=="1":
#        print("전체보기")
#        for i in list:
#            i=i[:i.rindex(".")]
#            print(i)

#    elif myNum=="2":
#        user=input("검색 단어: ")
#        for i in list:
#            if user in i:
#                file=open(i,'r',encoding='utf-8')
#                result=file.read()
#                print(result)
#                file.close()

#    elif myNum=="3":
#        user1=input("이름, 전화번호,지역을 입력: ")
#        f=user1 + ".txt"

#        file=open(f,'w',encoding="utf-8")
#        file.write(user1)
#        list.append(f)
#    elif myNum=="4":
#        print("종료")
#        break
#    else:
#        print("잘못된 입력입니다.")

friend1='이호진 01011112222 대구.txt'
friend2='홍길동 01022223333 서울.txt'
friend3='아아아 01055556666 경기도.txt'

list=[friend1,friend2,friend3]
while True:
    print("===================")
    print("1.전체보기")
    print("2.검 색")
    print("3.추 가")
    print("4.종 료")
    print("===================")
    myNum=input("메뉴 선택: ")
    if myNum=="1":
        print("전체보기")
        for i in list:
            i=i[:i.rindex(".")]
            print(i)

    elif myNum=="2":
        user=input("검색 단어: ")
        for i in list:
            if user in i:
                file=open(i,'r',encoding='utf-8')
                result=file.read()
                print(result)

    elif myNum=="3":
        user1=input("이름, 전화번호,지역을 입력: ")
        f=user1 + ".txt"

        file=open(f,'w',encoding="utf-8")
        file.write(user1)
        list.append(f)
    elif myNum=="4":
        print("종료")
        break
    else:
        print("잘못된 입력입니다.")