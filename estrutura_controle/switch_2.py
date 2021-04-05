def get_tipo_dia(dia):
    dias = {
        1: 'Fim de Semana',
        2: 'Dia de Semama',
        3: 'Dia de Semama',
        4: 'Dia de Semama',
        5: 'Dia de Semama',
        6: 'Dia de Semama',
        7: 'Fim de Semama'
    }

    return dias.get(dia, '***** Dia Invalida ******')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
