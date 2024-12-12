from session04 import Matrix
import numpy as np
import random

def is_same_matrix(mat_1:Matrix, mat_2:np.ndarray):
    col = mat_1.get_col()
    row = mat_1.get_row()

    return all(all(mat_1.get_data(r, c) == mat_2[r][c] 
                   for c in range(col))
                   for r in range(row))

# 무작위 배열 및 상수 선언
col = random.randint(3, 10)
row = random.randint(3, 10)
random_matrix = [
    [random.randrange(0, 100) for _ in range(col)] for __ in range(row)
]
numpy_1 = np.array(random_matrix)
Matrix_1 = Matrix(random_matrix)

random_matrix = [
    [random.randrange(0, 100) for _ in range(col)] for __ in range(row)
]
numpy_2 = np.array(random_matrix)
Matrix_2 = Matrix(random_matrix)

CONST = random.randint(1, 50)

# 행렬 합 비교
print(is_same_matrix(
    Matrix_1 + Matrix_2,
    numpy_1 + numpy_2))

# 행렬 차 비교
print(is_same_matrix(
    Matrix_1 - Matrix_2,
    numpy_1 - numpy_2))

# 행렬 요소곱 비교
print(is_same_matrix(
    Matrix_1 * Matrix_2,
    numpy_1 * numpy_2))

# 스칼라 요소곱 비교
print(is_same_matrix(
    Matrix_1 * CONST,
    numpy_1 * CONST))

# 행렬곱 비교
print(is_same_matrix(
    Matrix_1 @ Matrix_2.transpose(),
    numpy_1 @ numpy_2.transpose()))

# 전치 비교
print(is_same_matrix(
    Matrix_1.transpose(),
    numpy_1.transpose()))

# norm 비교
print(Matrix_1.norm() == np.linalg.norm(numpy_1))