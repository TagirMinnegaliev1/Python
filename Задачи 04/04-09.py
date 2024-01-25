num = int(input("Введите высоту пирамиды:"))
qwe = num - 1
z = 1
x = 2
for i in range(1, num+1):
    if i == 1:
        print(qwe * " ", "*", sep = "")
    else:
        if i % 2 == 0:
            print(qwe * " ", (i + z) * "*", sep = "")
            z += 2 
        else:
            print(qwe * " ", (i + x) * "*", sep = "")
            x += 2
            
    qwe -= 1