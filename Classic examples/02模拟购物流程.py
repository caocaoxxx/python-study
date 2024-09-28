lst=[]
for i in range(5):
    goods=input('请输入商品的名称和商品的编号进行入库,每次只能输出一个编号:')
    lst.append(goods)

for item in lst:
    print(item)
cart=[]
while True:
    flag=False
    num=input('请输入要购买的商品编号')
    for item in lst:
        if num==item[0:4]:
            flag=True
            cart.append(item)
            print('商品已添加至购物车')
            break #退出for循环
    if not flag and num!='q':
        print('商品不存在')
    if num=='q':
        break
cart.reverse()
print(f'您购物车的商品为:')
for item in cart:
    print(item)
