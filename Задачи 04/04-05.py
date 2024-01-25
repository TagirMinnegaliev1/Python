proizv = 1
for _ in range(6):
    num = int(input("Введите число:"))
    if num != 0:
        proizv *= num
print(proizv)