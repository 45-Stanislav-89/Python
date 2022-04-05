from sys import argv

name, time, salary, prem = argv
try:
    time = int(time)
    salary = int(salary)
    prem = int(prem)
    res = time * salary + prem
    print(f'Заработная плата: {res} тугриков')
except ValueError:
    print('Not a number')
