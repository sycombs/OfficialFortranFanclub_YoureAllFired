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

    def calculate_3bv(self):
        total = 0
        for i in range(self.height):
            for j in range(self.height):
                self.grid[i][j].isRevealed = False
        for i in range(self.height):
            for j in range(self.height):
                if not self.grid[i][j].isRevealed:
                    if self.grid[i][j].adj==0 and not self.grid[i][j].isBomb:
                        total+=1
                        self.recReveal(i,j)
        for i in range(self.height):
            for j in range(self.height):
                if not self.grid[i][j].isRevealed and not self.grid[i][j].isBomb:
                    total+=1
                    self.grid[i][j].isRevealed=True
        return total

    def recReveal(self, rows, cols):
        """ @pre    Grid is a valid object of type Board, rows and cols is the location in the board to reveal
            @post   will reveal all
            @return returns true if the cell in question is a mine, false if it is not
        """
        if rows>=self.height or rows<0 or cols>=self.width or cols<0 or self.grid[rows][cols].isRevealed:
            return
        self.grid[rows][cols].isRevealed=True

        if self.grid[rows][cols].isBomb:
            return

        elif self.grid[rows][cols].adj!=0:
            return

        elif self.grid[rows][cols].adj==0:

            self.recReveal(rows-1, cols-1)
            self.recReveal(rows-1, cols)
            self.recReveal(rows-1, cols+1)
            self.recReveal(rows, cols+1)
            self.recReveal(rows+1, cols+1)
            self.recReveal(rows+1, cols)
            self.recReveal(rows+1, cols-1)
            self.recReveal(rows, cols-1)


        return
