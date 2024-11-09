def month_to_season(num):
    if num < 1:
        num = 1
    if num > 12:
        num = 12
    if num in range(3, 5):
        return ("Весна")
    elif num in range(6, 8):
        return ("Лето")
    elif num in range(9, 11):
        return ("Осень")
    else:
        return ("Зима")


try:
    num = int(input("Введите номер месяца: "))
    print(month_to_season(num))
except ValueError:
    print("Введите пожалуйста целое число.")
