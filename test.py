# for i in range(2,10):
#     for y in range(1,10):
#         print(i, "X", y, "=", i*y)
#         if(y==9):
#             print("-----------------")

# for i in range(1, 10):
#     print("*"*i)

# for i in range(10,1,-1):
#     print("*"*i)
'''y=int(input('단수입력:'))
for i in range(1,10):
    print(y, 'X', i, '=', y*i)
x=int(input('값을 입력하시오.'))
if x>0:
    print(x, '는 양의 정수입니다.')
elif x<0:
    print(x, '는 음의 정수 입니다.')
else:
    print(x, '는 0 입니다.')'''
# i=1
# while i<9:
#     i=i+1
#     y=1
#     while y<10:
#         print(i, 'X', y, '=', i*y)
#         y+=1
#         if(y==10):
#             print('---------')
# for i in range(2,10):
#     for y in range(1,10):
#         print(i,'X',y,'=',i*y)
#         if (y==9):
#             print('-----------')

# for i in range(1,100):
#     if(i%2!=0 and i%3!=0):
#         print(i)
#
# i=1
# while i < 100:
#     if (i % 2 != 0 and i % 3 == 0):
#         print(i)
#     i += 1
# 연습문제 3-6
# import random
# while True:
#     num=random.randint(1, 10)
#     i=int(input('1~10사이의 숫자를 입력해주세요'))
#     if i==num:
#         print("정답입니다. 정답은%d" %(i))
#         break
#   연습문제 3-3
# i=(-1)+3+(-5)+7+(-9)
# y=9
# k=0
# while y<100:
#     k=i+y
#     y+=1
# print(k)
#연습문제 3-4
# i=1
# while i<11:
#     print('$'*i)
#     i+=1
#     if i==11 :
#         while i>1 :
#             i-=1
#             print('$'*i)
#         if i==1:
#             break
#
# for i in range(1, 11):
#     print('$'*i)
# for i in range(10, 0, -1):
#     print('$'*i)
#
# 1000 이하의 소수 구하기
# for i in range(2, 1001):
#     for y in range(2, i):
#         if i % y == 0:
#             break
#     else:
#         print(i)
#
#두숫자를 읽어 들여서 최대공약수 최소 공배수 구하기
# x=int(input("숫자를 입력해주세요"))
# y=int(input('숫자를 입력해 주세요'))
# gcd=0
# if x>y:
#     x, y=y, x
# for i in range(2, x+1):
#     if(x%i==0 and y%i==0):
#         gcd=i
# print("%d,%d의 최대 공약수는" %(x,y), gcd)
# lcm=(x*y)/gcd
# print("%d,%d의 최소 공배수는" %(x,y), lcm)
# 재귀 함수로 구하기
# def fun1(x,y):
#     if y==0:
#         return x
#     if x==y:
#         return x
#     return fun1(y, x%y)
# gcd= fun1(x, y)
# lcm=(x*y)/gcd
# print('%d 와 %d 의 최대공약수는' %(x,y), gcd)
# print('%d 와 %d 의 최소공배수는' %(x,y), lcm)
# 재귀함수로 n까지의 합 구하기
# def fun1(x):
#     if x<=0:
#         return 0
#     return x+fun1(x-1)
# print(fun1(100))
# score=[]
# y=0
# for i in range(1, 11):
#     score.append(input('학생명 과 점수를 입력해 주세요.\n'))
# while y< len(score):
#     print(score[y])
#     y+=1
# for v in score:
#     print(v)
# s={1,2,3,4,5}
# s.add(0)
# print(s)
# s.add(8)
# print(s)
# s.add(7)
# print(s)
# s.add('Hello')
# print(s)
# s.update()
#리스트에 딕셔너리 입력후 값추출하기
# lstudent=[]
# sumeng=0
# summath=0
# sumkorean=0
# avgeng=0
# avgmath=0
# avgkorean=0
# for i in range(0, 5):
#     lstudent.append(dict(name=input('%d번째 학생이름을 입력해 주세요.\n'%(i+1)),
#                          english=input('영어 점수를 입력해 주세요\n'),
#                          math=input('수학 점수를 입력해 주세요.\n'),
#                          korean=input('국어 점수를 입력해 주세요.\n')
#                          ))
# for i in lstudent:
#     sumeng+=int(i['english'])
#     summath+=int(i['math'])
#     sumkorean+=int(i['korean'])
# avgeng=sumeng/len(lstudent)
# avgmath=summath/len(lstudent)
# avgkorean=sumkorean/len(lstudent)
# print('영어\n총첨:%d\n평균:%f' %(sumeng, avgeng))
# print('수학\n총첨:%d\n평균:%f' %(summath, avgmath))
# print('국어\n총첨:%d\n평균:%f' %(sumkorean, avgkorean))
#메뉴명, 가격을 읽어드려서 list에 저장
# menu=[]
# name=input('메뉴명을 입력해주세요.')
# while name != '':
#     price = int(input('가격을 입력해주세요'))
#     d={'name': name, 'price': price}
#     menu.append(d)
#     name = input('메뉴명을 입력해주세요.')
# print(menu)
#반환값이 없는 함수로 구구단 출력 하기
# def gugudan(x,y):
#     print(x, "X", y, "=", x*y)
# for i in range (2, 10):
#     for j in range (1, 10):
#         gugudan(i, j)
#         if j==9:
#             print("-------------")

#반환값이 있는 함수로 구구단 출력 하기
def gugu(x, y):
    p=str(x)+'X'+str(y)+'='+str((x*y))
    return p
for i in range (2, 10):
    for j in range(1, 10):
        print(gugu(i, j))
        if j==9:
            print('-----------')
