class Calculator:
    def __init__(self, first, second, *data):
        self.first = first
        self.second = second
        self.data = data

    def plus(self):
        result = self.first + self.second
        return result

    def minus(self):
        result = self.first - self.second
        return result

    def multi(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first/self.second
        return result


def showUI(self):
    print("***** 계산기 *****")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")
    print("*****************")

calcApp=Calculator('shap','Pink', None)
#calcAPp.setData(3,4,5,6,7)
while True:
    calcApp.showUI()
    select=input("메뉴 선택")
    if select == '5': break

    elif select == '1':
         print(f'덧셈 => {calcApp.plus()}')

     #elif select == '2':









# c= calculator(a, b)
# print("덧셈", c.plus())
# print("뺄셈", c.minus())
# print("덧셈", c.multi())
# print("덧셈", c.div())
