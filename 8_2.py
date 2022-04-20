class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


div = lambda x, y: x / y if y != 0 else DivisionZero('На ноль делить нельзя')

print(div(6, 1))

print(div(8, 12))
