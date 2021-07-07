import os

# if not os.path.isdir('folder'):
#     os.mkdir('folder')

#os.chdir('TSIS5')
# os.chdir('..')

# if not os.path.isdir('nested/nested2/nesty'):
#     os.makedirs('nested/nested2/nesty')

# text_file = open('text.txt', mode='w', encoding='utf8')
# text_file.write('Это текстовый файл!')
# open('folder/text.txt', 'w', encoding='utf8').write("Это текстовый файл!?")
# print(os.stat('folder/text.txt'))
# print(os.stat('folder/text.txt').st_size)

# os.rename('text.txt', 'renamed-txt.txt')
# os.rename('folder', 'fold')
#os.replace('renamed-txt.txt', 'folder/renamed-txt.txt')
#os.replace('folder/renamed-txt.txt', '../renamed-txt.txt')

#print(os.listdir('folder'))

# распечатать все файлы и папки рекурсивно
for dir_path, dir_names, file_names in os.walk('.'):
      #перебрать каталоги
    for dir_n in dir_names:
        print(os.path.join(dir_path, dir_n))

      #перебрать файлы
    for file_n in file_names:
        print(os.path.join(dir_path, file_n))

# os.remove('folder/renamed-txt.txt')
#os.rmdir('nested')
#os.removedirs('nested/nested2/nesty') #удалит пустые каталоги

print(os.getcwd())

