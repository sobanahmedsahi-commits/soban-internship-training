items=[]
totalcost=0
maximum=-999999
minimum=999999
average=0
count=int(input("how many item prices do you want to enter: "))
for i in range(1,count+1):
    item=float(input("input your item price: "))
    items.append(item)
    totalcost+= item
    if item > maximum:
        maximum=item
    elif item < minimum:
        minimun=item
print(f"total cost is: {totalcost}")
average= totalcost / count
print("average price of the list is: ",average)