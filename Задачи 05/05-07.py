num = int(input())
war_with = "Евразия"
peace_with = "Остазия"

for _ in range(num):
    command = input()
    if command == "С кем война?":
        print(war_with)
    elif command == "С кем мир?":
        print(peace_with)
    elif command == "Меняем":
        war_with, peace_with = peace_with, war_with