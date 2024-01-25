num = int(input("Введите натуральное число:"))
count = 0

for i in range(1, num + 1):
    zxc = num / i
    if num % i == 0:
        count += 1
        if i != (num):
            print(i, end = " ")
        else:
            print(i)
if count == 2:
    print("Простое")
else:
    print("нет")