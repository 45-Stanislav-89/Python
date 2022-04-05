new_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(f'Исходный список: {(list(range(20, 241)))}')
print(f'Полученный список кратный 20 и 21: {new_list}')

