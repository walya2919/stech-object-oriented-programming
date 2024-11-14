class Block:
    def __init__(self, shape : list):
        self.shape = shape
    
    def rotate_clockwise(self):
        col = len(self.shape[0])
        row = len(self.shape)
        new_shape = [[self.shape[r][c] for r in range(row-1, -1, -1)] for c in range(col)]
        self.shape = new_shape
    
    def print_shape(self):
        for line in self.shape:
            print(line)