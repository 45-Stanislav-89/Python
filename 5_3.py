with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    poor = []
    p = 20000
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < p:
            poor.append(i[0])
        else:
            sal.append(i[1])
poor_str = ', '.join(poor)
print(f'Оклад меньше 20.000 имеют: {poor_str}.\nСредний оклад {sum(map(float, sal)) / len(sal)}')
