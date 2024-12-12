class Matrix:
    def __init__(self, data):
        # 주어진 data가 2차원 미만인지 검증
        try:
            self.row = len(data)
            self.col = len(data[0])
        except:
            raise ValueError
        #주어진 data가 3차원 이상인지 검증
        if not isinstance(data[0][0], int) and not isinstance(data[0][0], float):
            raise ValueError
        self.data = list(data)
    
    def get_data(self, row:int, col:int):
        return self.data[row][col]

    def get_col(self):
        return self.col
    
    def get_row(self):
        return self.row

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        
        if self.get_col() != other.get_col() or self.get_row() != other.get_row():
            raise ValueError
        
        new_data = [[self.get_data(i, j) + other.get_data(i, j)\
                    for j in range(self.get_col())]\
                    for i in range(self.get_row())]
        return Matrix(new_data)
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        
        if self.get_col() != other.get_col() or self.get_row() != other.get_row():
            raise ValueError
        
        new_data = [[self.get_data(i, j) - other.get_data(i, j)\
                    for j in range(self.get_col())]\
                    for i in range(self.get_row())]
        return Matrix(new_data)
    
    def __mul__(self, other):
        if not isinstance(other, Matrix) and not isinstance(other, int) and not isinstance(other, float):
            raise TypeError
        
        if isinstance(other, Matrix) and (self.get_col() != other.get_col() or self.get_row() != other.get_row()):
            raise ValueError
        
        if isinstance(other, int) or isinstance(other, float):
            other = Matrix([[other for _ in range(self.get_col())]for __ in range(self.get_row())])
        
        new_data = [[self.get_data(i, j) * other.get_data(i, j)\
                    for j in range(self.get_col())]\
                    for i in range(self.get_row())]
        return Matrix(new_data)
    
    def __rmul__(self, other):
        if not isinstance(other, Matrix) and not isinstance(other, int) and not isinstance(other, float):
            raise TypeError
        if isinstance(other, Matrix) and (self.get_col() != other.get_col() or self.get_row() != other.get_row()):
            raise ValueError
        
        if isinstance(other, int) or isinstance(other, float):
            other = Matrix([[other for _ in range(self.get_col())]for __ in range(self.get_row())])
        
        new_data = [[self.get_data(i, j) * other.get_data(i, j)\
                    for j in range(self.get_col())]\
                    for i in range(self.get_row())]
        return Matrix(new_data)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        
        if self.get_col() != other.get_row():
            raise ValueError
        
        left_row = self.get_row()
        inter_row_col = self.get_col()
        right_col = other.get_col()

        data = [[sum(self.get_data(r, i) * other.get_data(i, c)\
                     for i in range(inter_row_col))\
                        for c in range(right_col)]\
                            for r in range(left_row)]
        return Matrix(data)
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        if self.get_row() != other.get_row() or self.get_col() != other.get_col():
            raise ValueError

        return all(self.get_data(r, c) == other.get_data(r, c)\
                    for r in range(self.get_row())\
                    for c in range(self.get_col()))
    
    def transpose(self):
        data = [[0 for _ in range(self.get_col())] for __ in range(self.get_row())]
        for r in range(self.get_row()):
            for c in range(self.get_col()):
                data[r][c] = self.get_data(r, c)
        data = list(map(list, zip(*data)))
        return Matrix(data)
    
    def norm(self):
        sum_of_square = 0
        for r in range(self.get_row()):
            for c in range(self.get_col()):
                sum_of_square += self.get_data(r, c) ** 2
        
        return sum_of_square ** (1/2)

    def __str__(self):
        data = str()
        for r in range(self.get_row()):
            data += '['
            data += f'{self.get_data(r, 0)}'
            for c in range(1, self.get_col()):
                data += f', {self.get_data(r, c)}'
            data += ']\n'
        

        return '[' + data[:-1] + ']'