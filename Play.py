from Board import Board

def show(b):
    print("  ",end="")
    for i in range(b.width):
        print(" "+str(i)+" ",end="")
    print("")
    print("  ",end="")
    for i in range(3*b.width):
        print('-', end="")
    print("")
    for i in range(b.height):
        print(i, end="")
        print("|",end="")
        for j in range(b.width):
            if b.grid[i][j].isRevealed:
                if b.grid[i][j].adj == 0:
                    print(" _ ", end ='')
                else:
                    print(str(b.grid[i][j].adj), end ='')
            elif b.grid[i][j].isFlagged:
                print(" F ", end = '')
            else:
                print(" X ", end ='')
        print()

def run():
    """
    Max height and width prompts are set to tell user to put dimensions that we can handle.
    """
    height = int(input("Enter the height of the board"+"(Max height 24):"))
    while height > 24:
        height = int(input("please enter a height less than 25... try again"))
    width = int(input("Enter the width of the board:"+"Max width 24"))
    while width > 24:
        width = int(input("please enter a width less than 25... try again"))
    mines = int(input("Enter the number of mines:"))
    while mines >= height*width:
        mines = int(input("please use less than " + str(height*width) + " mines.  Try again: "))
    board = Board(height, width, mines)

    lose = False
    while not lose:
        """
         action = input("What would you like to do? Enter 'r' to reveal, 'f' to flag, or 's' to show:")
        if action == "r": text = "reveal"
        elif action == "f": text = "flag"
        else: text = ""
        row = input(f"For the cell you would like to {text}, enter row:")
        column = input(f"For the cell you would like to {text}, enter column:")
        """
        c = input("MENU \n Reveal: r x y\n Flag: f x y\n Show: s\n Quit: q \n <Prompt>: ")#TODO discuss possible promts, like turn counter
        a = c.split()[0]
        if a == "r" or a == "f":
            column, row = c.split()[1],c.split()[2]
            lose = click(board,int(row), int(column), a)
        elif c == "s":
            show(board)
        elif c == "q":
            break
        else:
            print("invalid Command")
            continue

def click(b,row, column, action):
    if action == "r":
        if b.grid[row][column].isBomb:
            return True
        else:
            b.grid[row][column].isRevealed = True
            return False
    elif action == "f":
        b.grid[row][column].isFlagged = True



run()