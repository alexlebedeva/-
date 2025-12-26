filename = input("Введите название файла: ")
test = input("Введите текст: ")
additional_text = input("Введите текст для добавления: ")



def write_in_file(filename, content):
    if content:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print("записано в файл")
    else:
        print("текст не введен")
    with open(filename, 'a',encoding='utf-8') as file:
        file.write(additional_text)
    print("Текст добавлен в файл")

write_in_file(filename, test)
print(f"Файл '{filename}' отредактирован")