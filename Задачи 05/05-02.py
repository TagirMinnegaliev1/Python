num = int(input())
bool = False
for i in range(num):
    str = input()
    if "кот" in str:
        bool = True
if bool:
    print("МЯУ")
else:
    print("НЕТ")