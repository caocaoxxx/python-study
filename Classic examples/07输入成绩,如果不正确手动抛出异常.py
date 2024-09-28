try:
    score=eval(input('请输入您的成绩:'))
    if score>=0 and score<=100:
        print(f'成绩为:{score}')

except BaseException:
    print('成绩不正确')
