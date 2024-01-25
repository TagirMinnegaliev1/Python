index = 0
list = []
while 1:
    str1 = input()
    index += 1
    if str1 == "СТОП":
        break
    else:
        if "кот" in str1:
            list.append(index)
        else:
            None
print("\n".join(map(str, list)))