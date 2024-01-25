list = []
num = 0
while 1:
    str = input()
    num += 1
    if "кот" or "Кот" in str:
        list.append(num)
    if str == "СТОП":
        print(list[0])
        break
        