def read_file(method='all'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if method == 'all':
                content = file.read()
                print(content)
            elif method == 'line':
                for line in file:
                    print(line, end='')
    except FileNotFoundError:
        print("Ошибка: нету такого файла  ")


filename = input("Имя файла:")
read_file('all')
read_file('line')