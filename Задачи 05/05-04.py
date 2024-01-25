num = int(input())
for i in range(num):
    str = input()
    if "кот" in str:
        bool = False
        print("МЯУ")
        break
    else:
        bool = True
if bool:
    print("НЕТ")