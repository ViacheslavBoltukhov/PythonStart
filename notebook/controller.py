import view
import read_note
import edit_a_note
import create_new_note
import delete_note
import get_all_notes
import show_list_notes
import write_note


def start():
    while True:
        mode = view.get_operating_mode()

        if mode == '1':  # 1 - Создать новую заметку
            new_note = create_new_note.create_note()
            write_note.write_note(new_note)

        elif mode == '2':  # 2 - Прочитать заметку
            notes = get_all_notes.get_all_notes()
            read_note.read_note(notes)

        elif mode == '3':  # 3 - Отредактировать заметку
            notes = get_all_notes.get_all_notes()
            edit_a_note.edit_note(notes)

        elif mode == '4':  # 4 - Удалить заметку
            notes = get_all_notes.get_all_notes()
            delete_note.delete_note(notes)

        elif mode == '5':  # 5 - Показать список заметок
            notes = get_all_notes.get_all_notes()
            show_list_notes.show_list_notes(notes)

        elif mode == '6':  # 6 - Выход из программы\n\
            print('\n' + 'Завершение работы.' + '\n')
            break
        else:
            print('Введите корректную команду')