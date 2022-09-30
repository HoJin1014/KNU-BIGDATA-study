# ----------------------------------------
# File & Dir 관련 모듈
# ----------------------------------------
import os.path  as path
import os

# 특정 폴더 존재여부 체크 => 폴더 없으면 폴더 생성하기
DIR_PATH='./Image/jpg/01'                    # 하위 폴더까지 생성       #경로로 보다가 DIR_PATH='./Image/jpg/02/000'
##DIR_PATH='./DATA'                       # 1개 폴더 생성
#print(path.exists(DIR_PATH))
if not path.exists(DIR_PATH):
    ##os.mkdir(DIR_PATH)                  # 1개 폴더 생성
    os.makedirs(DIR_PATH)                 # 하위 폴더까지 생성

# 특정 파일 존재 여부 체크 --------------------------------
DATA_FILE=DIR_PATH+'/flower.jpg';
if not path.exists(DATA_FILE):
    print('파일 없음')

# 특정 경로 안에 존재하는 내용 리스트 화 -------------------------
dataList=os.listdir('./AddressBook')
print(dataList)

# 시간 관련 모듈 ------------------------------------------------
import time as t

# 현재 시간
print(t.time())
print(t.localtime(t.time()))

curTime=t.localtime(t.time())
print(curTime.tm_year, curTime.tm_hour, curTime.tm_wday)
# 2022-06-24   2022/06/24    24/06/2022

for num in range(10):
    t.sleep(1.0)        #1초마다 넘어가게!     0.5도 설정가능
    #print(num)
    print('[num]', end='')



# num=0x4F
# num=0o7
# num=0b1010