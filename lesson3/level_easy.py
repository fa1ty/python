def user_data(name, age, city):
    list_date = '{}, {} лет, живёт в городе {}'.format(name, age, city)
    return list_date

def max_in_num_list(list_num):
    max_num = max(list_num)
    return max_num

def max_leng_in_list(*args):
    print(max(args, key=len))


while True:
    num = int(input('Введите номер задания: '))

    if num == 1:
        name = input('Введите Ваше имя: ')
        age = int(input('Введите Ваш возраст: '))
        city = input('Введите название города: ')
        date = user_data(name, age, city)
        print(date)

    elif num == 2:
        list_num = (21, 43, 76)
        max_num = max_in_num_list(list_num)
        print(max_num)

    elif num == 3:

        max_leng_in_list('Ананас', 'Айва', 'Груша', 'Киви', 'Мандарин')


    else:
        break