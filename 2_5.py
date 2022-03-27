my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг: {my_list}')
el = int(input("Введите натуральное положительное число: "))

while True:
    for i in range(len(my_list)):
        if my_list[i] is el:
            my_list.insert(i + 1, el)
            break
        elif my_list[0] < el:
            my_list.insert(0, el)
        elif my_list[-1] > el:
            my_list.append(el)
        elif my_list[i] > el and my_list[i + 1] < el:
            my_list.insert(i + 1, el)
            break
    print(f'Обновленный рейтинг: {my_list}')
    print('*' * 100)
    proceed = input('Продолжим (y/n)? ')
    if proceed == 'y':
        el = int(input('Введите натуральное положительное число: '))
    else:
        print('Пока!')
        break
