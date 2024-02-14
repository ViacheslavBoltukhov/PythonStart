def show_list_notes(all_notes):
    notes = all_notes
    notes.sort(key=lambda k: k[3])
    print()

    for line in notes:
        print(f'ID: {line[0]} \n'
              f'Заголовок: {line[1]} \n'
              f'Содержимое: {line[2]} \n'
              f'Дата изменения:  {line[3]} \n')