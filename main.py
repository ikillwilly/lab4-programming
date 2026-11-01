"""num = int(input("Введите целое число: "))
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
    print("Ноль")"""

""" a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
if (a >= b) and (a >=c):
    max = a
elif (b >= a) and (b >= c):
    max = b
else:
    max = c
print(f"Максимальное число: {max}") """

""" age = int(input("Введите возраст: "))
if age < 0:
    print("Некорректный возраст")
elif age <= 12:
    print("Ребёнок")
elif age <= 17:
    print("Подросток")
elif age <= 64:
    print("Взрослый")
else:
    print("Пожилой") """

""" import math
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
if a == 0:
    print("Это не квадратное уравнение")
else:
    d = b**2 - 4*a*c
    if d < 0:
        print("Нет решений")
    elif d == 0:
        print(f"x = {-b / (2*a)}")
    else:
        print(f"x1 = {(-b + math.sqrt(d))/ (2*a)}, x2 = {(-b - math.sqrt(d))/ (2*a)}") """

""" a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите действие (+, -, *, /): ").strip()
match operation:
    case "+":
        print(f"Результат: {a + b}")
    case "-":
        print(f"Результат: {a - b}")
    case "*":
        print(f"Результат: {a * b}")
    case "/":
        if b == 0:
            print("Деление на ноль")
        else:
            print(f"Результат: {a / b}")
    case _:
        print("Неизвестная операция") """

""" year = int(input("Введите год: "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год") """

""" a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Равносторонний треугольник")
    elif (a == b) or (a == c) or (b == c):
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Треугольник не существует") """

""" month = int(input("Введите номер месяца: "))
if (month == 12) or (month == 1) or (month == 2):
    print("Зима")
elif (month >= 3) and (month <= 5):
    print("Весна")
elif (month >= 6) and (month <= 8):
    print("Лето")
elif (month >= 9) and (month <= 11):
    print("Осень")
else:
    print("Некорректный номер месяца") """

""" import random
num = random.randint(1, 100)
guess = int(input("Введите число от 1 до 100: "))
while guess != num:
    if guess < num:
        print("Больше")
    else:
        print("Меньше")
    guess = int(input("Попробуйте ещё раз: "))
print("Вы угадали") """

""" num = input("Введите целое число: ")
if num.lstrip("-").isdigit():
    num = int(num)
    if num >= 0:
        print(f"Двоичная система: {bin(num)[2:]}")
        print(f"Восьмеричная система: {oct(num)[2:]}")
        print(f"Шестнадцатеричная система: {hex(num)[2:]}")
    else:
        print("Введите положительное число или ноль")
else:
    print("Ошибка ввода") """

""" height = float(input("Введите рост в метрах: "))
weight = float(input("Введите вес в кг: "))
if (weight <= 0) or (height <= 0):
    print("Ошибка ввода")
else:
    imt = weight / (height**2)
    print(f"ИМТ: {imt:.2f}")
    if imt < 18.5:
        print("Недостаточный вес")
    elif imt < 25:
        print("Норма")
    elif imt < 30:
        print("Избыточный вес")
    else:
        print("Ожирение") """

x = float(input("Введите x: "))
y = float(input("Введите y: "))
if (x == 0) and (y == 0):
    print("Точка находится в начале координат")
elif x == 0:
    print("Точка находится на оси Y")
elif y == 0:
    print("Точка находится на оси X")
elif (x > 0) and (y > 0):
    print("Первая четверть")
elif (x < 0) and (y > 0):
    print("Вторая четверть")
elif (x < 0) and (y < 0):
    print("Третья четверть")
else:
    print("Четвёртая четверть")