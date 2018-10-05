import random

class Cell:
    """
    Store data for each cell in the grid. Upon initiation, a Cell is not a bomb,
    not revealed, not flagged, and adjacent to no bombs.
    """
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
    """
    Maintains a 2D array of Cells. Maintains a height, a width, number of mines,
    and the number of Cells within it that are flagged. Upon initiation,
    randomly places the mines in the grid and updates each cells adjecency count
    accordingly.

    :param height: The height of the grid.
    :param width: The width of the grid.
    :param mines: The number of mines distributed across the Board.
    """
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
        """
        Prints the Board.
        """
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end="")
            print()

    def get_string_rep(self):
        a = []
        for i in self.grid:
            a.append(str(i))
        return a
