import os

def list_dir ():
    buffer = os.listdir()
    print('Список файлов:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))

if __name__ == '__main__':
    list_dir()