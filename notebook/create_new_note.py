import view
import datetime
import get_all_notes


def create_note():
    current_notes = get_all_notes.get_all_notes()
    all_ID = []
    all_title =[]

    for line in current_notes:
        all_ID.append(line[0])
        all_title.append(line[1])

    while True:
        note_ID = view.get_note_ID()
        if note_ID in all_ID:
            print("Данный ID уже существует. Введите другой: ")
        else:
            break

    while True:
        title = view.get_note_title()
        if title in all_title:
            print("Данный заголовок уже существует. Введите другой: ")
        else:
            break

    note_body = view.get_note_body()
    dt_now = datetime.datetime.now()


    return [note_ID, title, note_body, dt_now]