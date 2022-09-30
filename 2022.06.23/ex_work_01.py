# ----------------------------------------------
# 사용자가 입력한 댓글을 파일로 저장하기
# -----------------------------------------------
# - 키보드로 댓글 입력 받기
# - 입력 받은 댓글 누적 하기
# - 댓글 입력 종료 조건으로 q 또는 Q 입력시 댓글 입력 종료
# ------------------------------------------------

# input() 내장함수
# - 매개변수 : 입력받고 싶은 데이터 요청 메시지 => str 타입
# - 결과 : 입력받은 데이터 => str 타입
# ------------------------------------------------
#filename='comment.txt'

#with open(filename, mode='a', encoding='utf-8') as f:
    #while True:
      #  txt = input("댓글 입력: ")
      #  if txt in ['q', 'Q']: break
      #  print(f'txt => {txt}')
      #  f.write(txt+'\n')


#msg=input("댓글 입력")
#for i in range(1,10):
#    if i=='q' or i=='Q':
#       break
#print(msg)

# ----------------------------------------------
# [조건]
# - home.html 파일을 복사해서 home.txt 파일로 만들기
# - 함 수 명 : fileCopy
# - 매개변수 : 파일명
# - 반 환 값 : 없음
# -----------------------------------------------

#def fileCopy(filename):
    # 원본 파일 열고 데이터 꺼내기
#    srcFile=open(filename, mode='r', encoding='utf-8')
#    data=srcFile.read()
#    srcFile.close()

    # 복사본 파일에 데이터 쓰기
    #print(f"{filename.split('.')}")
##    filename=filename.split('.')[0]+'.txt'
    #'home.html'.index('.')
    #'home.html'.strip('.')
##    desFile=open(filename, mode='w', encoding='utf-8')
##    desFile.write(data)
##    desFile.close()

##fileCopy('./html/home.html')
##fileCopy('mydata.data')

##filename='./html/home.html'
##print(f'"."의 인덱스 => {filename.index(".")}')
##print(f'"."의 인덱스 => {filename.rindex(".")}')
##print(f'확장자 제거 => {filename[:filename.rindex(".")]}')



#filename='home.html'
#datas=filename.split('.')
#print(f'datas => {datas}, datas[0]=> {datas[0]}')

#print(filename.split('.')[0])



# 복사본 파일에 데이터 쓰기
#    filename=filename[:filename.rindex(".")]+'.txt'
#    desFile=open(filename, mode='w', encoding='utf-8')
#    desFile.write(data)
#    desFile.close()

def fileCopy(filename):
    # 복사 파일명 생성
    newFilename=filename[:filename.rindex(".")]+'.txt'
    # 파일 데이터 복사
    with open(filename, mode='r', encoding='utf-8') as srcFile:
        with open(newFilename, mode='w', encoding='utf-8') as srcFile:
            with open(newFilename, mode='w', encoding='utf-8') as desFile:
                desFile.write(srcFile.read())
