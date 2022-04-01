name = input("Как твоё имя? ")
print("Привет " + name + "!")

con = input("Откуда ты (страна)? ")
print(f"{con} - это отличная страна!")

knowledge = input("Ты хочешь изучить язык Python? да/нет ")
if knowledge == "да":
    print("Я помогу тебе в этом! ")
else:
    print("Не опускай руки, у нас все получится! ")

age = int(input("Сколько тебе лет? "))
my_age = 33
print(str(age), " - это хороший возраст. Мне ", int(my_age))

sum_age = age + my_age
print(f"Если сложить наш возраст, то получится - {age + my_age} - это шутка ;)",
      sep="")

print(f"Успехов тебе {name} которому(-ой_){age} лет!")
