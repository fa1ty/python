import os
import level_easy2
import level_easy


def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        return 'Выуспешно перешли в директорию {}'.format(dir_name)

    except FileNotFoundError:
        return 'Файла {} не существует'.format(dir_name)


def start():
    while True:
        print('Текущая директория ' + os.getcwd())
        num_for_chose = int(input('Выберете из списка:\n'
                                  '1. Перейти в папку.\n'
                                  '2. Посмотреть содержимое текущей папки.\n'
                                  '3. Удалить папку.\n'
                                  '4. Создать папку.\n'
                                  '0. Выйти.\n'))
        if num_for_chose == 1:
            dir_name = input('Введите название папки: ')
            print(change_dir(dir_name))
        elif num_for_chose == 2:
            level_easy2.list_dir()
        elif num_for_chose == 3:
            dir_name = input('Введите название папки: ')
            level_easy.del_dir(dir_name)
        elif num_for_chose == 4:
            dir_name = input('Введите название папки: ')
            level_easy.make_dir(dir_name)
        elif num_for_chose == 0:
            break
        else:
            print('Выберете из предложенного.')

























if __name__ == '__main__':
    start()