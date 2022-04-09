from random import randint

with open("text.txt", "w", encoding="utf-8") as my_w:
    my_list = [randint(1, 100) for _ in range(100)]
    my_w.write(" ".join(map(str, my_list)))

print(f"Сумма чисел в файле: {sum(my_list)}")