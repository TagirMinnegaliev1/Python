num = int(input())
found_cat = False
found_dog = False

for _ in range(num):
    str = input()
    if "Кот" in str or "кот" in str:
        found_cat = True
        found_dog = False
    if "Пёс" in str or "пёс" in str:
        found_dog = True

if found_cat and not found_dog:
    print("МЯУ")
else:
    print("НЕТ")