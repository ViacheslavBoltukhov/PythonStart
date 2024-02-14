import csv


def write_note(note):
    with open("Notes.csv", "a+", newline='', encoding="UTF-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(note)

    print('\n' + "Заметка успешно сохранена!" + '\n')