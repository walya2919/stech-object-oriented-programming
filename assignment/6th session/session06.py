from session04 import Matrix
import random


def save_matrix(mat:Matrix):
    save_str = mat.__str__().translate({ord(letter): '' for letter in '[]'})

    fp = open('save_matrix.txt', 'w')
    fp.write(save_str)
    fp.close()


col = random.randrange(3, 10)
row = random.randrange(3, 10)
matrix = Matrix([[random.randrange(1, 100) 
         for _ in range(col)] 
         for __ in range(row)])

save_matrix(matrix)