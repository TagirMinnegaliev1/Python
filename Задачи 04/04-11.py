import statistics

num = int(input("Кол-во тестируемых:"))
list = []
for i in range(num):
    iq = int(input())
    if i == 0:
        print(0)
    else:
        if iq == statistics.mean(list):
            print(0)
        elif iq > statistics.mean(list):
            print(">")
        else:
            print("<")
    list.append(iq)