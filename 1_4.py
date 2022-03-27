n = (int(input("Введите целое положительное число: ")))
num_max = n % 10
while n > 1:
    n = n // 10
    if n % 10 > num_max:
        num_max = n % 10
    if n > 9:
        continue
    else:
        print("Самая большая цифра в этом числе: ", num_max)
        break

