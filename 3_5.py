def my_f():
    z = 0
    while True:
        m_list = input('Введите числа для сложения или "r" для выхода: ').split()
        for num in m_list:
            if num.lower() == "r":
                return z
            else:
                try:
                    z = z + int(num)
                except ValueError:
                    print('Что бы выйти, нажмите "r"')
        print(f'Сумма чисел равена: {z}')


print(my_f())
