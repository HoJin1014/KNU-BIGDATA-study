# ----------------------------------------------------------
# 현대 자동차를 표현하는 데이터 타입 즉 class 생성
# 클래스명 : car
# 속성/특징 : 제조사, 차번호, 차종류, 색상
#           -> 클래스   변수:
#           -> 인스턴스 변수:
# 역할/기능 : 이동한다, 정지한다, 차정보 출력한다.
#           -> 이동한다 => 000 자동차가 ㅇㅇ에서 ㅇㅇ로 간다.
#           -> 정지한다 => 000 자동차가 ㅇㅇ에 정지한다.
#           -> 차정보출력한다. => 제조사, 차종류, 차번호
# -----------------------------------------------------------
# 숫자 10개 저장하기
# nums=[]
# for n in range(10):
#     nums.append(str(input("enter number :")))
class car:

    # 클래스 변수
    brand = "현대"


    # 인스턴스 객체 생성 및 초기화 함수
    def __init__(self, carNum, carType, carColor):
        self.carNum = carNum
        self.carType = carType
        self.carColor = carColor

    # car 클래스 기능 및 역할 메서드
    def move(self, strat, end):
        print(f'{self.carNum}자동차가 {start}에서 {end}로 이동한다.')

    def stop(self, target):
        print(f'{self.carNum}자동차가 {target}에서 정지한다.')

    def displayInfo(self):
        print(f'번  호 : {self.carNum}')
        print(f'종  류 : {self.carType}')
        print(f'색  상 : {self.carColor}')
        print(f'제조사 : {car.brand}')

# 자동차 데이터 저장 => 자동차 인스턴스 생성 => 클래스명() __init__()
myCar=car(1234,'suv','hotpink')
myCar.move('경북대학교', '경주')
myCar.displayInfo()


# 정수 10 => car 데이터 10개 저장
nums=[]
for n in range(10): nums.append(n*10)

cars=[]
for n in range(10):
    num, type, color = input("차번호, 차종류, 차색상 : ").split(',')
    cars.append( car(num, type, color) )
   #cars.append(n*1111, 'suv', 'black')

for car in cars:
    print(f'{car.carNum}')
    car.displayInfo()







# class car:
#
#     car="현대자동차"
#
#     def __init__(self, made, carNum, carType, color):
#         self.made = made
#         self.carNum = carNum
#         self.carType = carType
#         self.color = color
#
#
#     def move(self, home):
#         print(f'{car.carNum}은 {home}으로 이동한다.')
#
#     def stop(self, traffic):
#         print(f'{car.carNum}은 {traffic}에서 정지한다.')
        
    