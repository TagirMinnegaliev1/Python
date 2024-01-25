login = input("Введите логин:")
email = input("Введите резервную почту:")
if "@" not in login and "@" in email:
    print("OK")
elif "@" in login and "@" in email:
    print("Неверно указан логин")
elif "@" not in login and "@" not in email:
    print("Неверно указан вдрес резервной почты")
else:
    print("Неверно указан логин и адрес резервной почты")