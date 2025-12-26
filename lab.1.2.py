try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a > b:print(("большее число:" ), a )
    elif a == b:print("числа одинаковые" ),
    else:print(("большее число:" ), b )
except ValueError: print("Ошибка! Вы ввели не число!!!!!!")