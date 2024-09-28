num = int(input("请输入一个整数："))
flag = False
for i in range(2,num):
    if num % i == 0:
        flag = True
        break
if flag:
    print(f'{num}不是素数')
else:
    print(f'{num}是素数')