import os

path = input('Путь к файлу: ')
append_name = input('Какое имя добавить к файлу? ')
exp_name = input('Напишите желаемое расширение файла (без точки): ')

list_of_files = os.listdir(path)
files_len = len(list_of_files)
result_names = [i.split('.jpg')[0] for i in list_of_files]

for i in range(0, files_len):
	os.rename(path + '\\' + list_of_files[i], path + '\\' + result_names[i]  + append_name + '.' + exp_name)

new_list_of_files = os.listdir(path)
decision = input('Вернуть исходные имена файлов [y(англ)+Enter - да, Enter - нет]\n')
if decision == 'y':
	for i in range(0, files_len):
		os.rename(path + '\\' + new_list_of_files[i],  path + '\\' + list_of_files[i])
