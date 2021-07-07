import os
import os.path
from pathlib import Path


def file_w():
    s2 = input()
    if s2 == 'del':
        print("Enter name of file")
        try:
            file = input()
            os.remove(file)
            print('File deleted')
        except FileNotFoundError:
            print('Error')

    elif s2 == 'ren':
        print('Enter name of file')
        try:
            file = input()
            print("Enter the new name")
            file_n = input()
            os.rename(file, file_n)
        except FileNotFoundError:
            print('Error')

    elif s2 == 'add':
        print('Enter the name of file to add data')
        try:
            file = input()
            with open(file, 'w') as file:
                file.write(input())
            print('Data added successfully')
        except FileNotFoundError:
            print('Error')

    elif s2 == 'rew':
        print('Enter the name of file to rewrite')
        try:
            file = input()
            with open(file, 'w') as file:
                file.write(input())
            print('Data rewrote successfully')
        except FileNotFoundError:
            print("Error")

    elif s2 == 'ret':
        print("Enter full path")
        try:
            file = input()
            path = Path(file).parent
            print(path)
        except FileNotFoundError:
            print("Error")


def direct_w():
    s2 = input()
    if s2 == 'ren':
        print('Enter name of directory')
        try:
            file = input()
            print('Enter the new name')
            file_n = input()
            os.rename(file, file_n)
        except FileNotFoundError:
            print("Error")

    elif s2 == 'numf':
        try:
            path, dirs, files = next(os.walk(input()))
            file_count = len(files)
            print(file_count)
        except FileNotFoundError:
            print("Error")

    elif s2 == 'numd':
        with os.scandir(input()) as entries:
            cnt = 0
            for entry in entries:
                if entry.is_dir():
                    cnt += 1
        print(cnt)

    elif s2 == 'lsd':
        try:
            print('List content of the directory:')
            for dir_path, dir_names, file_names in os.walk('.'):
                # перебрать каталоги
                for dir_n in dir_names:
                    print(os.path.join(dir_path, dir_n))
                # перебрать файлы
                for file_n in file_names:
                    print(os.path.join(dir_path, file_n))
        except FileNotFoundError:
            print('Error')

    elif s2 == 'adf':
        print('Enter the name of file to add data')
        try:
            file = input()
            with open(file, 'w') as file:
                file.write(input())
            print('Data added successfully')
        except FileNotFoundError:
            print('Error')

    elif s2 == 'add':
        print('Enter the name of directory to add data')
        try:
            d = input()
            if not os.path.isdir(d):
                os.mkdir(d)
        except FileNotFoundError:
            print('Error')
    elif s2 == 'del':
        print("Enter name of directory")
        try:
            dirt = input()
            os.rmdir(dirt)
            print('Directory deleted')
        except FileNotFoundError:
            print('Error')


selection = input()

if selection == 'Help':
    print("Select an action:", '\n')
    print('Your current location in directory. Select "1".')
    print('Work with a directory or a file. Select "2".')
    print('-> Select an option: work with directory - "2", work with file - "1".')
    print('\tYour current location is file. You have several options:')
    print('\t\t delete file - "del".')
    print('\t\t rename file - "ren".')
    print('\t\t add content to this file - "add".')
    print('\t\t rewrite content of this file - "rew".')
    print('\t\t return to the parent directory - "ret".')
    print('\tYour current location is directory. You have several options:')
    print('\t\t rename directory - "1".')
    print('\t\t print number of files - "2".')
    print('\t\t print number of directories - "3".')
    print('\t\t list content of the directory - "4".')
    print('\t\t add file to this directory - "5".')
    print('\t\t add new directory to this directory - "6".')

elif selection == '1':
    print("Your current location: " + str(os.getcwd()))

elif selection == '2':
    selec = input()
    if selec == '1':
        file_w()

    elif selec == '2':
        direct_w()


# made by Yernar Naryshov