try:
    Userinput = input("введите целое число: ")
    n = int(Userinput)
    if n < 1:
        print("введите число больше нуля.")
    else:
        for i in range(1, n + 1):
            print(i)
except ValueError:
    print("Ошибка! ВЫ ввели не число.")