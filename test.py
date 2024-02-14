def get_body_mass_index(m, l):
    ind = m / l
    if ind < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= ind <= 25:
        print('Норма')
    else:
        print('Избыточная масса тела')
