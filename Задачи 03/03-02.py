password1 = input("Введите пароль: ")
password2 = input("Введите пароль: ")

if len(password1) < 8:
    print("Короткий!")
elif password1 != password2:
    print("Различаются.")
else:
    print("OK")