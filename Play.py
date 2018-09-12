from Board import Board

def promptCheck(prompt):
    """
    Checks for valid inputs at the menu prompt.
    :param prompt: The input provided by the user as a string.
    :return: True if the input is valid, False otherwise.
    """
    arr = prompt.split(" ")
    if arr[0] not in ["r", "f", "q"]:
        return False
    if arr[0] == "r" or arr[0] == "f":
        if len(arr) < 3:
            return False
        try:
            int(arr[1])
            int(arr[2])
        except ValueError:
            return False
    return True

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
            print("Pick a whole number, silly goose... try again.")
            continue
        else:
            return userInput

def show(b):
    """
    shows current state of board in command line
    :param Board b:
    :return None:
    """
    print("   ", end="")
    for i in range(b.width):
        print(" "+f"{i: 2}"+" ", end="")
    print()
    print("  ", end="")
    for i in range(b.width):
        print('----', end="")
    print()
    for i in range(b.height):
        print(f"{i: 2}", end="")
        print("|",end="")
        for j in range(b.width):
            if b.grid[i][j].isFlagged:
                print("  F ", end='')
            elif b.grid[i][j].isRevealed:
                if b.grid[i][j].adj == 0:
                    print("  _ ", end='')
                else:
                    print("  "+str(b.grid[i][j].adj)+" ", end='')
            else:
                print("  X ", end='')
        print()

def run():
    """
    Max height and width prompts are set to tell user to put dimensions that we can handle.
    """
    height = inputNumber("Enter the height of the board: ")
    while height > 24:
        height = inputNumber("Please enter a height less than 25... try again.")
    while height < 2:
        height = inputNumber("You have to have at least a height of 2... try again.")
    width = inputNumber("Enter the width of the board: ")
    while width > 24:
        width = inputNumber("Please enter a width less than 25... try again.")
    while width < 2:
        width = inputNumber("You have to at least have width of 2... try again.")
    mines = inputNumber("Enter the number of mines: ")
    while mines >= height*width:
        mines = inputNumber(f"Please use less than {height*width} mines... try again.")
    while mines <= 0:
        mines = inputNumber("You have to have at least 1 bomb, silly goose... try again.")
    board = Board(height, width, mines)
    show(board)

    lose = False
    flaggedBombCount = 0

    while not lose and flaggedBombCount != board.mines:
        c = input("MENU:\n Reveal Square: r x y\n Add or Remove Flag: f x y\n Quit: q\n <Prompt>: ").lower() #TODO discuss possible prompts, like turn counter
        if promptCheck(c):
            a = c.split()[0]
            if a == "r" or a == "f":
                column, row = int(c.split()[1]), int(c.split()[2])
                lose = click(board, row, column, a)
                if board.grid[row][column].isBomb and board.grid[row][column].isFlagged:
                        flaggedBombCount += 1
                show(board)
            elif a == "q":
                break
        else:
            print("Invalid command. Pick a whole number, silly goose... try again.")

    if lose:
        print("Bomb detonated! You need more practice, young grasshopper.")
    elif c == "q":
        print("Thank you for playing... come again!")
    else:
        print("*Mario Voice* You are the weiner!")

def click(b,row, column, action):
    """
    selects cell to perform intended action on
    :param Board b, int row, int column, string action:
    :return Bool lose:
    """
    if action == "r":
        if b.grid[row][column].isBomb:
            return True
        elif b.grid[row][column].isFlagged:
            print("You can't reveal a flagged square. Please remove the flag and try again.")
            return False
        else:
            spread(b,row,column)
            return False
    elif action == "f":
        if b.grid[row][column].isFlagged:
            b.flagCount -= 1
            b.grid[row][column].isFlagged = False
        else:
            if b.flagCount == b.mines:
                print("You cannot use more flags than bombs... remove a flag to place another;\n"
                      "place a flag on a square that has a flag in order to remove it.")
            else:
                b.flagCount += 1
                b.grid[row][column].isFlagged = True
        return False

def spread(b,row,column):
    """
    Reveals adjacent cells
    :param Board b, int row, int column:
    :return None:
    """
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

if __name__ == '__main__':
   run()
