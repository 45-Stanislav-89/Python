from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
result = reduce(lambda x, y: x * y, my_list)
print(f'Четные числа из диапазона 100-1000: {my_list}')
print(f'Результат произведения четных чисел из списка: {result}')
