# 저장 된 txt 파일 읽어 오기

#readlines()사용하기
# f = open('d:/temp/menu.txt', mode='r', encoding='utf-8')
# lines = f.readlines()
# for row in lines:
#     ar=row.split(",")
#     print('메뉴명=', ar[0], ',','가격=', ar[1], end='')
# f.close()

#readline()사용하기
# f = open('d:/temp/menu.txt', mode='r', encoding='utf-8')
# line=f.readline()
# while line!='':
#     ar=line.split(",")
#     print('메뉴명=', ar[0], ',', '가격=', ar[1], end='')
#     line=f.readline()
# f.close()

#데이터 파일 저장하기
f = open('d:/temp/menu1.txt', mode='w', encoding='utf-8') #없으면 만들어서 열고, 있으면 열고
f.write("아메리카노")
f.write("라떼")
f.close()

f = open('d:/temp/menu1.txt', mode='w', encoding='utf-8') #없으면 만들어서 열고, 있으면 열고
f.writelines(["아메리카노","라떼"])
f.close()