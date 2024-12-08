SEPARATOR = '------------------------------------------'

def main_menu(n_parameter):
        while True:
            print(SEPARATOR)
            option = int(input('ГЛАВНОЕ МЕНЮ\n'
                               '1 - Ввести или обновить информацию\n'
                               '2 - Вывести информацию\n'
                               '0 - Завершить работу\n'
                               'Введите номер пункта меню: '))
            if option == 0:
                break
            elif option == 1:
                withdraw_or_update()
            elif option == 2:
                information_output(n_parameter)


#Ввести или обновить информацию
def withdraw_or_update():
    while True:
        print(SEPARATOR)
        option1 = int(input('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n'
                            '1 — Личная информация\n'
                            '2 — Информация о предпринимателе\n'
                            '0 — Назад\n'
                            'Введите номер пункта меню: '))
        if option1 == 0:
            break
        elif option1 == 1:
            n_parameter = input('Введите имя: ')
        elif option1 == 2:
            pass
    return n_parameter

#Вывести информацию
def information_output(n_parameter=withdraw_or_update()):
    while True:
        print(SEPARATOR)
        option1 = int(input('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n'
                            '1 — Общая информация\n'
                            '2 — Вся информация\n'
                            '0 — Назад\n'
                            'Введите номер пункта меню: '))
        if option1 == 0:
            break
        elif option1 == 1:
            print(n_parameter)
        elif option1 == 2:
            pass

def main():
    name, age, telephone, email, index, postalcode = '', 0, '', '', '', ''
    print('Приложение MyProfile\n'
          'Сохраняй информацию о себе и выводи ее в разных форматах')
    print(SEPARATOR)
    main_menu(name)


if __name__ == '__main__':
    main()