num = int(input("Введите целое число: "))
if num % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
if num % 3 == 0:
    print("Делится на 3")
else:
    print("Не делится на 3")
if num > 0:
    print("Положительное")
elif num < 0:
    print("Отрицательное")
else:
    print("Ноль")