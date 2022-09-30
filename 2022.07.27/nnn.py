def addCost_1():
    total=list(menuCost_1.values())
    filename='주문.txt'
    #filename = ',' + t.strftime('%Y-%m-%d %A %I:%M:%S') + '.txt'
    # 파일명 리스트 추가
    # CtmBook 폴더에 파일 생성
    with open(IFM_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(str(total[0]))