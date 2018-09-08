import random

class Cell:
    def __init__(self):
        self.isBomb = False
        self.isRevealed = False
        self.isFlagged = False
        self.adj = 0

    def __repr__(self):
        if self.isBomb:
            return "X"
        return str(self.adj)

class Board:
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.grid = []
        self.flagCount = 0
        for i in range(height):
            temp = []
            for j in range(width):
                temp.append(Cell())
            self.grid.append(temp)
        loc = []
        for i in range(height):
            for j in range(width):
                loc.append((i, j))
        random.shuffle(loc)
        for i in range(mines):
            row = loc[i][0]
            col = loc[i][1]
            self.grid[row][col].isBomb = True
            if row-1 >= 0:
                self.grid[row-1][col].adj += 1
                if col-1 >= 0:
                    self.grid[row-1][col-1].adj += 1
                if col+1 < width:
                    self.grid[row-1][col+1].adj += 1
            if row+1 < height:
                self.grid[row+1][col].adj += 1
                if col-1 >= 0:
                    self.grid[row+1][col-1].adj += 1
                if col+1 < width:
                    self.grid[row+1][col+1].adj += 1
            if col-1 >= 0:
                self.grid[row][col-1].adj += 1
            if col+1 < width:
                self.grid[row][col+1].adj += 1

    def displayBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end="")
            print()

# test = Board(10, 10, 1)
# test.displayBoard()
