def my_f(word):
    latin = input('Введите слово из маленьких латинских букв')
    return word.title() if not set(word).difference(latin) else False


stroka = input('Введите строку из слов разделенных пробелом: ').split()
for i in stroka:
    result = my_f(i)
    if result:
        print(result, ' ')
