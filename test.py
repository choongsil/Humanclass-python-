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
for i in range(2,10):
    for y in range(1,10):
        print(i,'X',y,'=',i*y)
        if (y==9):
            print('-----------')