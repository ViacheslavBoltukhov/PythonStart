import csv
import view

def delete_note(all_notes):
    notes = all_notes
    found_index = -1
    index_line = 0
    title = view.get_note_title()

    for line in notes:
        if line[1] == title:
            print('Текущее содержание заметки: ' + line[2])
            found_index = index_line
        index_line += 1

    if found_index > -1:
        notes.pop(found_index)

        with open("Notes.csv", "w", newline='', encoding="UTF-8") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(notes)

        print('\n' + "Заметка успешно удалена!" + '\n')
    else:
        print("Заметка не найдена")