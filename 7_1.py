class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
my_m2 = Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)
