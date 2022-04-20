revenue = float(input("Введите значение выручки фирмы: "))
costs = float(input("Введите значение издержек фирмы: "))
if revenue - costs > 0:
    print(f"Ваша фирма работает в прибыль! Размер вашей прибыли составляет {revenue - costs:+0.1f} руб.")
    print(
        f"Рентабельность составляет {(revenue - costs) / costs * 100:+0.1f}%")
    workers = int(input("Введите число сотрудников вашей фирмы: "))
    print(
        f"Прибыль фирмы в расчете на одного сотрудника составляет {(revenue - costs) / workers:+0.1f} руб."
        f" или {((revenue - costs) / workers) * 100 / (revenue - costs):+0.1f}%")
elif revenue - costs == 0:
    print("Ваша фирма работает ничего не заработала и ничего не потеряла!")
else:
    print(f"Ваша фирма работает в убыток. Размер вашего убытка составляет {-costs - revenue} руб.")
