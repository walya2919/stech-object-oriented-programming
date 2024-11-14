from block import Block

class Pane():
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

    def display(self, block:Block):
        screen = [[0 for _ in range(self.width)] for __ in range(self.height)]
        block_row = len(block.shape)
        block_col = len(block.shape[0])
        for col in range(block_col):
            for row in range(block_row):
                if block.shape[row][col] == 1:
                    screen[row][col] = 1
        
        for line in screen:
            print(" ".join(map(str, line)))