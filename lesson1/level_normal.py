def ex1():
    pass



print('Привет, пользователь!')
print('Если хотите выйти введите "q"')
num = ''

while num != 'q':
    print('Введите "3", чтобы выйти из подпрограммы')
    num = int(input('Введите номер задания(1, 2): '))

    if num == 1:
        n = ''
        while n != 'q':
            n = int(input('Введите число от 1 до 10: '))
            if n >= 1 or n <= 10:
                print(n * n)
                break
            else:
                print('Вы ввели не верное число')
                n = int(input('Введите число от 1 до 10: '))

    elif num == 2:
        a = int(input('Введите первое число '))
        b = int(input('Введите второе число '))
        a = a + b
        b = a - b
        a = a - b
        print('Первая переменная = ', a)
        print('Вторая переменная = ', b)
    elif num == 3:
        break
    else:
        print('Вы ввели неизвестное значение')


print('Вы вышли из программы. До свидания!')