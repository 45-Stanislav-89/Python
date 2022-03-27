# Version 1 (dict)
num_month = int(input("Введите номер месяца: "))

calendar = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
                 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
if num_month in calendar:
    print(calendar.get(num_month))


# Version 2 (list)
num_month = int(input("Введите номер месяца: "))
calendar_2 = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']
for i, b in enumerate((calendar_2), 1):
    if num_month is i:
        print(b)
