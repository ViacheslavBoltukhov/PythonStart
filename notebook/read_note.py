import view

def read_note(all_notes):
    title = view.get_note_title()
    notes = all_notes
    for line in notes:
        if line[1] == title:
            print("\n" + "Содержимое заметки: "+line[2] + "\n")
            break
    else:
        print('Заметка не найдена')