YEAR=2022
#import
def printYear():
    print(f'올해는 {YEAR}')


for i in range(5):
    printYear()

if __name__ == '__main__':
    for i in range(5): printYear()
print(f'[ex_func] __name__ => {__name__}')