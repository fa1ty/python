import math
import random


while True:

    num = int(input('Введите номер задания: '))

    if num == 1:
        a1 = [1, 3, 2, 4, 6, 7, 25, 9]
        res = [int(math.sqrt(i)) for i in a1 if i > 0 and math.sqrt(i).is_integer()]
        print(res)

    elif num == 2:
        date = '05.09.2005'
        list_date = date.split('.')
        days = {
            '01': 'первое',
            '02': 'второе',
            '03': 'третье',
            '04': 'четвёртое',
            '05': 'пятое',
            '06': 'шестое',
            '07': 'седьмое',
            '08': 'восьмое',
            '09': 'девятое',
            '10': 'десятое',
            '11': 'одиннадцатое',
            '12': 'двенадцатое',
            '13': 'тринадцатое',
            '14': 'четырнадцатое',
            '15': 'пятнадцатое',
            '16': 'шестнадцатое',
            '17': 'семнадцатое',
            '18': 'восемнадцатое',
            '19': 'девятнадцатое',
            '20': 'двадцатое',
            '21': 'двадцать первое',
            '22': 'двадцать второе',
            '23': 'двадцать третье',
            '24': 'двадцать четвёртое',
            '25': 'двадцать пятое',
            '26': 'двадцать шестое',
            '27': 'двадцать седьмое',
            '28': 'двадцать восьмое',
            '29': 'двадцать девятое',
            '30': 'тридцатое',
            '31': 'тридцать первое',
        }
        months = {
            '01': 'января',
            '02': 'февраль',
            '03': 'марта',
            '04': 'апреля',
            '05': 'мая',
            '06': 'июня',
            '07': 'июля',
            '08': 'августа',
            '09': 'сентября',
            '10': 'октября',
            '11': 'ноября',
            '12': 'декабря',
        }

        result = f'Сегодня {days.get(list_date[0])} {months.get(list_date[1])} {list_date[2]} года.'
        print(result)

    elif num == 3:
        n = int(input('Введите количество цифр в списке: '))
        # if n >= 20:
        #     print('Введите число поменьше')
        a = []
        for _ in range(n):
            ran = random.randint(-100, 100)
            a.append(ran)
        print(a)

    elif num == 4:
        lst = [1, 2, 4, 5, 6, 2, 5, 2]
        first = list(set(lst))
        print(first)

    elif num == 5:
        lst = [1, 2, 4, 5, 6, 2, 5, 2]
        lst2 = []
        for i in lst:
            if lst.count(i) == 1:
                lst2.append(i)
        print(lst2)

    elif num == 0:
        break