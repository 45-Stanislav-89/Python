my_list = input("Введите элементы списка: ")
numbers = list(my_list)
x = 0
for i in range(int(len(numbers) / 2)):
    numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
    x += 2
print(numbers)
