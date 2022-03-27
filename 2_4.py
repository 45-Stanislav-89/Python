line = input('Введите несколько слов, отделяя их пробелами:')

my_list = line.split()
for i, n in enumerate(my_list, 1):
    print(f'{i}) {n[:10]}')
