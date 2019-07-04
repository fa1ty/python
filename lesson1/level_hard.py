print('Добро пожаловать в программу "Медицинская карточка"')

name = input('Введите Ваши имя и фамилию: ')
age = int(input('Введите Ваш возраст: '))
weight = int(input('Введите Ваш вес: '))

if age < 30:
    if 50 < weight < 120:
        print('Имя: ', name, 'возраст: ', age, 'Вес: ', weight, '- у Вас хорошее состояние')
    elif weight > 120 or weight < 50:
        print('Имя: ', name, 'возраст: ', age, 'Вес: ', weight, '- Вам следует следить за своим здоровьем')
elif 40 <= age >= 30:
    if weight < 120 or weight > 50:
        print('Имя: ', name, 'возраст: ', age, 'Вес: ', weight, '- Вам следует следить за своим здоровьем')
    elif weight > 120 or weight < 50:
        print('Имя: ', name, 'возраст: ', age, 'Вес: ', weight, '- Вам необходимо обратиться к врачу')
elif age > 40:
    if weight < 120 or weight > 50:
        print('Имя: ', name, 'возраст: ', age, 'Вес: ', weight, '- Вам следует следить за своим здоровьем')
    elif weight > 120 or weight < 50:
        print('Имя: ', name, 'возраст: ', age, 'Вес: ', weight, '- Вам срочно нужен врач')
