num = int(input("Кол-во секунд:"))

if num >=0:
    for i in range(num + 1):
        print(f"Осталось секунд: {num - i}")
        if i == num:
            print("Пуск!")
else:
    print("Пуск!")