with open('text_4_1.txt', 'w', encoding='utf-8') as my_w, \
        open('text_4.txt', 'r', encoding='utf-8') as my_r:
    t = (my_r.read().split('\n'))
    for i in t:
        i = i.split()
        if (i[0]) == 'One':
            i[0] = 'Один'
        if (i[0]) == 'Two':
            i[0] = 'Два'
        if (i[0]) == 'Three':
            i[0] = 'Три'
        if (i[0]) == 'Four':
            i[0] = 'Четыре'
        u = (' '.join(i))
        my_w.write(f'{u}\n')
