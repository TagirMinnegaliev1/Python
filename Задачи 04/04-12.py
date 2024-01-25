amount = int(input())
result = 0
for i in range(amount):
    num = int(input())
    if i % 3 == 0:
        result += num
    elif i % 3 == 1:
        result -= num
    else:
        result += num
print(f"Результат: {result}")