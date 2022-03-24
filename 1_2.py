time_sec = int(input("Введите время в секундах: "))

hour = time_sec // 3600
min_sec = time_sec % 3600
min = min_sec // 60
sec = min_sec % 60

x = ":"

print (f"{hour:02}{x}{min:02}{x}{sec:02}")
