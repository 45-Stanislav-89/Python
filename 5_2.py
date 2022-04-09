with open('text_4.txt', 'r', encoding='utf-8') as my_f:
    b = my_f.readlines()
    print(f'Кол-во строк в файле: {len(b)}')

    my_f = open('text_4.txt', 'r', encoding='utf-8')
    c = my_f.readline()

    for i in range(len(b)):
        print(f'В {i + 1} строке - {len(c.split())} слова')
