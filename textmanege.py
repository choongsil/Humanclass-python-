# 저장 된 txt 파일 읽어 오기

#readlines()사용하기
# f = open('d:/temp/menu.txt', mode='r', encoding='utf-8')
# lines = f.readlines()
# for row in lines:
#     ar=row.split(",")
#     print('메뉴명=', ar[0], ',','가격=', ar[1], end='')
# f.close()

#readline()사용하기
f = open('d:/temp/menu.txt', mode='r', encoding='utf-8')
line=f.readline()
while line!='':
    ar=line.split(",")
    print('메뉴명=', ar[0], ',', '가격=', ar[1], end='')
    line=f.readline()
f.close()