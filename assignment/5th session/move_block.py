from block import Block

class Pane():
    def __init__(self, width:int, height:int, block:Block, x_position=0, y_position=0):
        self.width = width
        self.height = height
        self.block = block
        self.x_position = x_position
        self.y_position = y_position
    
    def display(self):
        screen = [[0 for _ in range(self.width)] for __ in range(self.height)]
        block_row = len(self.block.shape)
        block_col = len(self.block.shape[0])
        try:
            for col in range(block_col):
                for row in range(block_row):
                    if self.block.shape[self.y_position + row][self.x_position + col] == 1:
                        screen[self.y_position + row][self.x_position + col] = 1
        except IndexError:
            print("블록이 게임판 범위를 벗어났습니다.")
            return