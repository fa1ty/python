import os, shutil

def start():
    if os.path.isfile('level_easy3.py'):
        newFile = 'level_easy3.py' + ".copy"
        shutil.copy('level_easy3.py', newFile)
        if os.path.exists(newFile):
            print("Файл", newFile, "создан")
        else:
            print("Произошла ошибка")

if __name__ == '__main__':
    start()