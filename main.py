# MyProfile app

SEPARATOR = '------------------------------------------'

# Личная информация
name = ''
age = 0
phone = ''
email = ''
index = ''
postalcode = ''
# Информация о предпринимателе
ogrnip = ''
inn = ''
current_account = 0
name_bank = ''
bic = 0
correspondent_account = 0


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter, p_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', i_parameter)
    print('Почтовый индекс:', p_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 — Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                index = input('Введите индекс: ')
                postalcode = input('Введите почтовый адрес: ')


            elif option2 == 2:
                # input social links
                while True:
                    ogrnip = input('Введите ОГРНИП: ')
                    if len(ogrnip) == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')
                inn = input('Введите ИНН: ')
                while True:
                    current_account = input('Введите расчетный счет: ')
                    if len(current_account) == 20:
                        break
                    else:
                        print('Расчетный счет должен содержать 20 цифр')
                name_bank = input('Введите название банка: ')
                bic = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счет: ')

            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, postalcode)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, postalcode)

                # print social links
                print('')
                print('Информация о предпринимателе ')
                print('ОГРНИП:', ogrnip)
                print('ИНН: ', inn)
                print('Банковские реквизиты ')
                print('Р/с:   ', current_account)
                print('Банк: ', name_bank)
                print('БИК:', bic)
                print('К/с: ', correspondent_account)