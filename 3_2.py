def my_f(**kwargs):
    return ' '.join(kwargs.values())


print(my_f(Имя=(input('Имя: ')), Фамилия=(input('Фамилия: ')), Год_рождения=(input('Год рождения: ')),
           Город_проживания=(input('Город проживания: ')), Email=(input('Email: ')), Телефон=(input('Телефон: '))))
