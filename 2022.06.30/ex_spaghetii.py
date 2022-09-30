class Spaghetti:
    def __init__(self, noodle, source, taste):
        self.noodle = noodle
        self.source = source
        self.taste = taste

    def cookNoodle(self):
        print(f'{self.noodle} 삶는다.')

    def cookMix(self):
        print(f'{self.noodle}과 {self.source}소스와 면을 섞는다.')

    def cookTaste(self):
        print(f'{self.taste} 맛 본다.')

    def fininsh(self):
        print('잘 먹었습니다.')



def selectMenu():
    print("--- 스파게티 요리")
    print(" ")