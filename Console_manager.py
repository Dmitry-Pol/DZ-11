import os
import shutil
import glob
import sys
import victory
import use_functions

print(__name__)

def add_folder():
    folder = input('введите имя папки')
    user_path = os.path.join(os.getcwd(), folder)
    if os.path.exists(user_path):
        print('Такая папка уже существует')
    else:
        os.mkdir(user_path)
    pass

def del_file_folder():
    folder = input('введите имя папки')
    user_path = os.path.join(os.getcwd(), folder)
    if os.path.exists(user_path):
        os.rmdir(user_path)
    else:
        print('Такой папки не существует')
    pass

def copy_file_folder():
    folder = input('введите имя копируемого файла')
    shutil.copy(folder, folder.split('.')[0]+'_new.'+folder.split('.')[1])

def view_dir():
    print(os.listdir())

def view_folder():
    print(list(os.walk(os.getcwd()))[0][1])

def view_file():
    print(glob.glob(os.path.join(os.getcwd(), '*.*')))

def view_OS():
    print(sys.path)
    print(sys.executable)

def view_creator():
    print('creator programm - D. Poleshchenko')

def play_victorina():
    victory.vic()

def bank_():
    use_functions.bank()

# def exit_(dic):

user_path = os.getcwd()

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        add_folder()
    elif choice == '2':
        del_file_folder()
    elif choice == '3':
        copy_file_folder()
    elif choice == '4':
        view_dir()
    elif choice == '5':
        view_folder()
    elif choice == '6':
        view_file()
    elif choice == '7':
        view_OS()
    elif choice == '8':
        view_creator()
    elif choice == '9':
        play_victorina()
    elif choice == '10':
        bank_()
    elif choice == '11':
        break
    else:
        print('Неверный пункт меню')


