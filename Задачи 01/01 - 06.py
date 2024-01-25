question1 = input("Любите ли вы котиков? (да/нет): ").lower()
question2 = input("Умеете ли вы программировать? (да/нет): ").lower()
if question1 == "да" and question2 == "да":
    print("МЕГАХАРОШ.")
elif question1 == "да" and question2 == "нет":
    print("НОРМ.")
elif question1 == "нет" and question2 == "да":
    print("ХАРОШ.")
elif question1 == "нет" and question2 == "нет":
    print("ПЛОХ.")
else:
    print("Ошибка: ответьте на вопросы 'да' или 'нет'.")
