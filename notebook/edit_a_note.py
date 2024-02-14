import csv
import datetime
import view


def edit_note(all_notes):
    notes = all_notes
    found_index = -1
    index_line = 0
    title = view.get_note_title()

    for line in notes:
        if line[1] == title:
            print("\n" + 'Текущее содержимое заметки: ' + line[2] + "\n")
            found_index = index_line
        index_line += 1

    if found_index > 0:
        notes[found_index][1] = view.get_new_note_title()
        notes[found_index][2] = view.get_new_body()
        notes[found_index][3] = datetime.datetime.now()

        with open("Notes.csv", "w", newline='', encoding="UTF-8") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(notes)

        print('\n' + "Заметка успешно изменена!" + '\n')
    else:
        print("Заметка не найдена")