# -------------------------------------------------
# PATH
# - 절대경로 : 파일 및 폴더 존재하는 위치의 경로 예) C:\Users\anece\.....
# - 상대경로 : 현재 코드 파일 기준으로 경로를 지정
#  . -> 현재위치
# .. -> 상위 한단계 위
# -------------------------------------------------
file=r'D:\Android\media\com.samsung.android.spay'
file='../Data/home.html'
file='./html/home.html'

# -------------------------------------------------
# home.html 파일을 라인 단위로 읽어서 화면에 출력하기
# -------------------------------------------------
# 파일열기
file=open(file, mode='r', encoding='utf-8')

# 파일읽기
#data=file.read()
#print(f'all data => {data}')
while True:
    data=file.readlines()
    if not data: break
    data = data.strip()
    if len(data)>0: print(data)



    #data=data.lstrip(__chars='\n')
    #if not data: break
    #print(f'line data => {data}')

# 파일닫기
file.close()

# with ~ as 구문
with open(file, mode='r', encoding='utf-8') as file:
    while True:
        data = file.readline()
        if no data: break
        data = data.strip()
        if len(data)>0:print(data)

#f=open("C:/doit/home.html", mode='r')
#data=file.read()
#print(f'read data => {data}')
#print(f'read data type => {type(data)}')