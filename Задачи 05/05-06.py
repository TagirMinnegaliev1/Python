list = []
count = 0
sum = 0
while 1:
    num = int(input())
    count += 1
    if num == 0:
        print(list[0])
        break
    else:
        sum += num
        if sum == 10:
            qwe = count
            list.append(qwe)