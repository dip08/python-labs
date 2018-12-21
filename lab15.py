import copy
A = [[1, 4, 3, 4],
     [3, 2, 7, 1],
     [2, 5, 2, 8],
     [9, 9, 3, 2]]


def determinant(matrix):
    # столбцы
    n = len(matrix)
    # строки
    m = len(matrix[0])
    if n != m:
        return None
    elif n == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(n):
            B = copy.deepcopy(matrix)
            del B[0]
            for j in range(n - 1):
                del B[j][i]
            det += matrix[0][i] * (-1) ** i * determinant(B)
        return det


for i in A:
    print(i)
print(determinant(A))
