def my_f(x, y):
    z = (abs(x) ** y)
    print(f'Число {x} в степени {y} равно: {z}')


my_f(float(input('Введите действительное положительное число: ')), int(input('Введите отрицательное число: ')))
