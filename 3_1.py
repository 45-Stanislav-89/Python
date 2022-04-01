def del_num(a, b):
    print(f'Полученный результат: {a / b:.3}')


try:
    del_num(float(input('Введите первое число: ')), float(input('Введите второе число: ')))
except (ZeroDivisionError):
    print('На ноль делить нельзя')
except (ValueError):
    print('Некорректный ввод')
