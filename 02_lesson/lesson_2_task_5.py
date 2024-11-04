def month_to_season(num):
    if num in range(3, 5):
        print("Весна")
    elif num in range(6, 8):
        print("Лето")
    elif num in range(9, 11):
        print("Осень")
    else:
        print("Зима")


month_to_season(1)
