for i in range(17):
    d = int(input())
    try:
        if i % d == 0:
            print("ДА")
        else:
            print("НЕТ")
    except ZeroDivisionError:
        print("Число не должно равняться 0!!!") 