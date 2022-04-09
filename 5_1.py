my_list = []
while True:
    line = input("Введите данные: ")
    if line == '':
        print(my_list)
        break
    else:
        new_line = line + '\n'
        my_list.append(new_line)

    with open("5_1.txt", "w", encoding='utf-8') as file_obj:
        file_obj.writelines(my_list)
