import random


# BADDY BAD BAD BAD
def convert_cell_to_dictionary(someCell):
    cellDict = {'isBomb': someCell.isBomb,
                'isRevealed': someCell.isRevealed,
                'isFlagged': someCell.isFlagged,
                'adj': someCell.adj}
    return cellDict


def convert_dictionary_to_cell(someDict):
    cell = Cell()
    cell.isBomb     = someDict['isBomb']
    cell.isRevealed = someDict['isRevealed']
    cell.isFlagged  = someDict['isFlagged']
    cell.adj        = someDict['adj']

    return cell


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

    def brute_force(self, cell, i, j):
        self.grid[i][j] = cell


# Create a board
aBoard = Board(4, 4, 1)

# Print it
print("Board A")
aBoard.displayBoard()
print("")

# Create a new board
bBoard = Board(4, 4, 5)

# Print it
print("Board B")
bBoard.displayBoard()
print("")

# Replace the first board with the new one
for r in range(0, bBoard.height):
    for c in range(0, bBoard.width):
        tempCell = convert_cell_to_dictionary(bBoard.grid[r][c]) # Yes, test it like this
        # because of networking stuff
        send_comm(tempCell, plyr1, plyr2)

for r in range(0, plyr2Board.height):
    for c in range(0, plyr2Board.width):
        # Keep getting data
        newCell  = convert_dictionary_to_cell(tempCell)
        aBoard.brute_force(newCell, r, c)

# Print the first board again
print("New Board A")
aBoard.displayBoard()
