def month_to_season(mounth):
    if mounth in range(1, 3):
        print("Зима")
    elif mounth in range(3, 6):
        print("Весна")
    elif mounth in range(6, 9):
        print("Лето")
    elif mounth in range(9, 12):
        print("Осень")
    elif mounth == 12:
        print("Зима")
    else:
        print("Число выходит из диапозона")


month_to_season(int(input("Введите число месяца: ")))
