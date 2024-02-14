
def get_operating_mode():
    print('''1 - Создать новую заметку
2 - Прочитать заметку
3 - Отредактировать заметку
4 - Удалить заметку
5 - Показать список заметок
6 - Выход из программы''')
    op_mode = input('Выберите команду: ')
    return op_mode

def get_note_ID():
    id = input('Введите ID новой заметки:')
    return id

def get_note_title():
    title = input('Введите заголовок заметки: ')
    return title

def get_new_note_title():
    title = input('Введите новый заголовок заметки: ')
    return title

def get_note_body():
    body = input('Введите тело заметки:')
    return body

def get_new_body():
    body = input('Введите новое содержимое заметки:')
    return body