lst = [
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',400]
]
print('编号\t\t名称\t\t品牌\t\t单价\t\t')

#格式化
for row in lst:
    row[0]='0000'+row[0]
    row[3]='￥{0:.2f}'.format(row[3])
    
for row in lst:
    for item in row:
        print(item,end="\t\t")
    print()
