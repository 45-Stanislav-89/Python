import json

with open("my_ex7.json", "w", encoding="utf-8") as my_f:
    with open("text_7.txt", encoding="utf-8") as my_r:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_r}
        result = [profit, {"profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                           len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, my_f, ensure_ascii=False, indent=4)
