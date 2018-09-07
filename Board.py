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
        self.board = []
        for i in range(height):
            temp = []
            for j in range(width):
                temp.append(Cell())
            self.board.append(temp)
        loc = []
        for i in range(height):
            for j in range(width):
                loc.append((i, j))
        random.shuffle(loc)
        for i in range(mines):
            row = loc[i][0]
            col = loc[i][1]
            self.board[row][col].isBomb = True
            if row-1 >= 0:
                self.board[row-1][col].adj += 1
                if col-1 >= 0:
                    self.board[row-1][col-1].adj += 1
                if col+1 < width:
                    self.board[row-1][col+1].adj += 1
            if row+1 < height:
                self.board[row+1][col].adj += 1
                if col-1 >= 0:
                    self.board[row+1][col-1].adj += 1
                if col+1 < width:
                    self.board[row+1][col+1].adj += 1
            if col-1 >= 0:
                self.board[row][col-1].adj += 1
            if col+1 < width:
                self.board[row][col+1].adj += 1

    def displayBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j], end="")
            print("\n", end="")

test = Board(10, 10, 1)
test.displayBoard()
