import random

"""
Store data for each cell in the grid.
"""
class Cell:
    """
    Initiates a Cell. Upon initiation, a Cell is not a bomb, not revealed, not flagged, and adjacent to no bombs.
    """
    def __init__(self):
        self.isBomb = False
        self.isRevealed = False
        self.isFlagged = False
        self.adj = 0
    """
    Controls how a Cell is represented. Bombs are represented by Xs; other Cells are represented by the number of adjacent bombs.
    """
    def __repr__(self):
        if self.isBomb:
            return "X"
        return str(self.adj)

"""
Maintains a 2D array of Cells.
"""
class Board:
    """
    Initiates a Board. Maintains a height, a width, number of mines, and the number of Cells within it that are flagged.
    Upon initiation, randomly places the mines in the grid and updates each cells adjecency count accordingly.
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
    """
    Prints the Board.
    """
    def displayBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end="")
<<<<<<< HEAD
            print()
=======
            print()


>>>>>>> 2dc43ce10ba947bd3b53748b7bfd0cdc0d3d10cb
