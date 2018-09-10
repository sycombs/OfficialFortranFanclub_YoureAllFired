from Board import Board




def inputNumber(prompt):
    """
    catches inputs by user for anything other than an integer.
    :param prompt: string
    :return: int userInput
    """
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Pick a whole number silly goose... try again")
            continue
        else:
            return userInput

def show(b):
    print("   ", end="")
    for i in range(b.width):
        print(" "+f"{i:02}"+" ", end="")
    print()
    print("  ", end="")
    for i in range(b.width):
        print('----', end="")
    print()
    for i in range(b.height):
        print(f"{i:02}", end="")
        print("|",end="")
        for j in range(b.width):
            if b.grid[i][j].isRevealed:
                if b.grid[i][j].adj == 0:
                    print("  _ ", end='')
                else:
                    print("  "+str(b.grid[i][j].adj)+" ", end='')
            elif b.grid[i][j].isFlagged:
                print("  F ", end='')
            else:
                print("  X ", end='')
        print()

def run():
    """
    Max height and width prompts are set to tell user to put dimensions that we can handle.
    """
    height = inputNumber("Enter the height of the board: ")
    while height > 24:
        height = inputNumber("please enter a height less than 25... try again ")
    while height < 2:
        height = inputNumber("You have to have at least a height of two... try again ")
    width = inputNumber("Enter the width of the board: ")
    while width > 24:
        width = inputNumber("please enter a width less than 25... try again ")
    while width < 2:
        width = inputNumber("you have to at least have width of two... try again ")
    mines = inputNumber("Enter the number of mines: ")
    while mines >= height*width:
        mines = inputNumber("please use less than " + str(height*width) + " mines.  Try again: ")
    while mines <= 0:
        mines = inputNumber("You have to have at least 1 bomb silly goose... try again ")
    board = Board(height, width, mines)
    show(board)

    lose = False
    flaggedBombCount = 0

    while not lose and flaggedBombCount != board.mines:
        """
         action = input("What would you like to do? Enter 'r' to reveal, 'f' to flag, or 's' to show:")
        if action == "r": text = "reveal"
        elif action == "f": text = "flag"
        else: text = ""
        row = input(f"For the cell you would like to {text}, enter row:")
        column = input(f"For the cell you would like to {text}, enter column:")
        """
        c = input("MENU \n Reveal Square: r x y\n Flag: f x y\n Quit: q \n <Prompt>: ")#TODO discuss possible promts, like turn counter
        a = c.split()[0]
        if a == "r" or a == "f":
            column, row = int(c.split()[1]),int(c.split()[2])
            lose = click(board,(row), (column), a)
            if board.grid[row][column].isBomb and board.grid[row][column].isFlagged:
                    flaggedBombCount += 1
            show(board)
        elif c == "q":
            break
        else:
            print("invalid Command")
            continue

    if lose:
        print("Bomb detonated: You need more practice young grasshopper")
    elif c == "q":
        print("Thank you for playing... come again")
    else:
        print("you are the weiner! (Mario Voice)") #FIXME triggers even if quit option selected

def click(b,row, column, action):
    if action == "r":
        if b.grid[row][column].isBomb:
            show(b)
            return True
            
        else:
            
            spread(b,row,column)
            show(b)
            return False
    elif action == "f":
        if b.grid[row][column].isFlagged:
            b.flagCount -= 1
            b.grid[row][column].isFlagged = False
        else:
            if b.flagCount == b.mines:
                print("Cannot use more flags than bombs... remove a flag to place another; \n"
                      "place a flag on a square that has a flag in order to remove it")
            else:
                b.flagCount += 1
                b.grid[row][column].isFlagged = True
        return False

def spread(b,row,column):
    if (b.grid[row][column].adj >0 or b.grid[row][column].isRevealed):
        b.grid[row][column].isRevealed=True
        return
    else:
        b.grid[row][column].isRevealed=True
        if row-1 >= 0:
            spread(b,row-1,column)
        if row+1 < b.height:
            spread(b,row+1,column)
        if column-1 >= 0:
            spread(b,row,column-1)
        if column+1 < b.width:
            spread(b,row,column+1)
        return

run()