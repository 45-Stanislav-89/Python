from itertools import count, cycle

for a in count(int(input('Введите целое число: '))):
    if a > 10:
        break
    print(a)
print('*' * 40)

c = 0
for el in cycle(['Привет', 5, 'Пока']):
    if c > 5:
        break
    print(el)
    c += 1
print('*' * 40)
