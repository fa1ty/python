def ex1():
    a = 25
    b = 'ps'
    c = ''
    print(a, b, c)
    sumf = input('Введите что-нибудь: ')
    if sumf:
        print(sumf)
    else:
        print('Вы ничего не ввели')
def ex2():

    n = int(input('Введите число: '))
    print(n + 2)

def ex3():
    age = int(input('Введите Ваш возраст: '))
    if age >= 18:
        print("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")

print('Привет, пользователь!')
print('Если хотите выйти введите "q"')
num = ''

while num != 'q':
    print('Введите "4", чтобы выйти из подпрограммы')
    num = int(input('Введите номер задания(1, 2, 3): '))

    if num == 1:
        ex1()
    elif num == 2:
        ex2()
    elif num == 3:
        ex3()
    elif num == 4:
        break
    else:
        print('Вы ввели неизвестное значение')
        num = input('Введите номер задания(1, 2 или 3): ')


print('Вы вышли из программы. До свидания!')


