def Sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=num*num
    return sum

num=eval(input('请输入一个整数： '))
print(f'前{num}个数的平方和为',Sum(num))