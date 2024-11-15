from block import Block

class Pane():
    def __init__(self, width:int, height:int, block:Block, x_position=0, y_position=0):
        self.width = width
        self.height = height
        self.block = block
        self.x_position = x_position
        self.y_position = y_position
    
    def __print_screen(self, screen:list):
        for line in screen:
            print(" ".join(map(str,line)))
        print()

    def display(self):
        screen = [[0 for _ in range(self.width)] for __ in range(self.height)]
        block_row = len(self.block.shape)
        block_col = len(self.block.shape[0])
        if self.x_position<0 | self.y_position<0 | self.width<self.x_position+block_col | self.height<self.y_position+block_row:
            print("[warning] 블록이 게임판 범위를 벗어났습니다.")
            return
        
        # todo: 블록 위치에 대한 조건 더 생각해보기

        # elif any(screen[self.y_position+row][self.x_position+col]==1 & self.block.shape[row][col]==1 for row in range(block_row) for col in range(block_col)):
        #     print("[warning] 블록이 이전에 설치된 블록과 겹칩니다.")
        #     return

        for row in range(block_row):
            for col in range(block_col):
                if self.block.shape[row][col]==1:
                    screen[self.y_position+row][self.x_position+col]=1
        self.__print_screen(screen)
        return
    
    def drop(self):
        if self.y_position + len(self.block.shape) < self.height:
            self.y_position += 1
            self.display()
            return
        else:
            print("[wanging] 블록이 바닥에 도달했습니다.")
            return

    def move_left(self):
        if self.x_position > 0:
            self.x_position -= 1
        self.display()
        return
    
    def move_right(self):
        if self.x_position + len(self.block.shape[0]) < self.width:
            self.x_position += 1
        self.display()
        return