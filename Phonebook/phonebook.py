'''Создать телефонный справочник с возможностью импорта и экспорта данных вформате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные и сохранять данные в текстовом файле.
Пользователь может ввести одну и характеристик для поиска определенной записи
(Например имя или фамилию человека).
Использование функций. Ваша программа не должна быть линейной.
1. Создать файл для записи телефонной книги.         ++++++++
открытие файла на дозапись.
Подготовка меню для пользователя.                  +++++++++
3. Запись данных в файл по каждому контакту:
ввод данных пользователя,                           +++++
подготовка данных для записи в файл,                +++++
открытие файла в режиме дозаписи,                   +++++
запись новой строки с данными                       +++++
4. Чтение данных из файла:                          +++++++
открытие файла в режиме чтения,                     ++++++++++
считать все данные и вывести их на экран.           ++++++
Поиск записей по параметрам и вывод соответствующих данных
ввод пользователем параметра поиска,
открыть файл в режиме чтения,
считать все данные из файла и сохранить их в программе,
сделать выборку нужной записи - сам поиск,
показать результат поиска.'''



def input_name():
    return input("Введите имя контакта: ")


def input_surname():
    return input("Введите фамилию контакта: ")


def input_patronymic():
    return input("Введите отчетство контакта: ")


def input_phone():
    return input("Введите телефон контакта: ")


def input_adress():
    return input("Введите адрес контакта: ")


def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_contact = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(str_contact)


def read_file():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()


def print_data():
    print(read_file())


def search_contact():
    print("Варианты для поиска:\n"
          "1) Фамилия\n"
          "2) Имя\n"
          "3) Отчество\n"
          "4) Телефон\n"
          "5) Адрес")
    command = input("Укажите вариант поиска: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод номера варианта!\n"
              "Повторите ввод")
        command = input("Укажите номер варианта: ")
    print()
    i_search_param = int(command) - 1
    search = input("Введите данные для поиска: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    # print(contacts_list)

    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        # print(contact_lst)
        if search in contact_lst[i_search_param]:
            print(contact_str + "\n")

def copy_contact():
    contacts_list = read_file().rstrip().split("\n\n")
    for num, elem in enumerate(contacts_list,1):
        print(num, elem)
    i_search_param = int(input('Введите номер копируемого контакта: ')) - 1
    while len(contacts_list) < i_search_param:
        print('Контакта с таким порядковым номером не существует')
        i_search_param = int(input('Введите номер копируемого контакта: ')) - 1
    with open("phonebook_copy.txt", "a", encoding="UTF-8") as file:
        file.write(contacts_list[i_search_param] + "\n\n")

def interface():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    command = ""
    while command != "5":
        print("Выберите вариант работы с телефонной книгой:\n"
              "1) Запись данных\n"
              "2) Вывод телефонной книги на экран\n"
              "3) Поиск данных\n"
              "4) Копирование\n"
              "5) Выход"
              )
        command = input("Введите номер операции: ")
        while command not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод номера операции!\n"
                  "Повторите ввод")
            command = input("Введите номер операции: ")
        print()

        match command:
            case "1":
                input_data()
            case "2":
                print_data()
            case "3":
                search_contact()
            case "4":
                copy_contact()
            case "5":
                print("Приложение закрыто!")




interface()