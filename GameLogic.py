"""@package docstring
GameLogic.py (or, MineSweeper.py) should deal with the handling of the game's
run time logic.

Question: Maybe both client AND server side logic should be handled here. Since
we're currently looking at three different game modes, we can throw all of our
logic here and then just have the three modes do everything on their own?

That way there's no need to worry about client/server stuff if you're in
single player mode
"""
from Board import *
from colorama import Fore, Style
import time
import player
import pickle
from Server import *
from Leaderboard import *
from Time import *

def receive_pickle(serverSocket):
    '''
    TODO: get this working
    attempts to receive multiple packets by pickle
    '''
    print ("Receiving Pickles now:")
    end = b'\x00\x00END_MESSAGE!\x00\x00'[:blocksize]
    blocks = []
    while True:
        blocks.append(serverSocket.recv(blocksize))
        print ("doin stuff?")
        if blocks[-1] == end:
            blocks.pop()
            break
    data = b''.join(blocks)

    print ("about to return unpickled stuff")
    return data

def mult_start_inp(player, board=None):
    '''
    @brief called on game start to initialize players in multiplayer game,
    1st decides board parameters
    '''
    if player.send_player_state() == b'inp':
        #b'inp' means this is first player so set id to 1
        player.playerData['ID'] = 1
        #ask for board input (only first player)
        board_params = game_input()
        #msg in playerdata is used to convey any string info, could add more elements
        player.playerData['msg'] = " ".join(str(x) for x in board_params)
        player.send_player_state()
        return receive_pickle(serverSocket)

    elif player.send_player_state() == b'p2':
        player.playerData['ID'] = 2
        print ("Welcome to Minesweeper!\nThe board parameters are:")
        print("Height: " + board_params[0] + "\nWidth: " + board_params[1] + "\nMines: " + board_params[2])





def show(board, lose=False):
    """
    Shows current state of board in command line.

    :param Board board: The current Board object.
    :return None:
    """
    print("   ", end="")
    for i in range(board.width):
        print(" " + f"{i:02}" + " ", end="")
    print()
    print("  ", end="")
    for i in range(board.width):
        print('----', end="")
    print()
    for i in range(board.height):
        print(f"{i:02}", end="")
        print("|",end="")
        for j in range(board.width):
            if board.grid[i][j].isFlagged:
                print(Fore.RED + "  F ", end='')
            elif board.grid[i][j].isRevealed:
                if board.grid[i][j].adj == 0:
                    print(Fore.GREEN + "  _ ", end='')
                else:
                    print(Fore.CYAN + "  " + str(board.grid[i][j].adj)+ " ", end='')
            elif lose:
                if board.grid[i][j].isBomb:
                    print(Fore.MAGENTA + "  B ", end='')
                else:
                    print(Fore.WHITE + "  X ", end="")
            else:
                print(Fore.WHITE + "  X ", end="")
        print(Style.RESET_ALL)

def cheat_show(board):
    """
    Fully displays board, regardless of reveals/flags.

    :param Board board: The current Board object.
    :return None:
    """
    print("   ", end="")
    for i in range(board.width):
        print(" " + f"{i:02}" + " ", end="")
    print()
    print("  ", end="")
    for i in range(board.width):
        print('----', end="")
    print()
    for i in range(board.height):
        print(f"{i:02}", end="")
        print("|",end="")
        for j in range(board.width):
            if board.grid[i][j].isBomb:
                print(Fore.MAGENTA + "  B ", end='')
            elif board.grid[i][j].adj == 0:
                print(Fore.GREEN + "  _ ", end='')
            else:
                print(Fore.CYAN + "  " + str(board.grid[i][j].adj)+ " ", end='')
        print(Style.RESET_ALL)

def cheatMode(board):
    """
    Activates cheat mode, which reveals the entire board. Only accessible in single-player mode.

    :param Board board: The current Board object.
    :return None:
    """
    #board.displayBoard(); for checking correct output
    cheat_show(board);
    for x in range(1, 6):
        print (f"{x}...")
        time.sleep(1)

def inputNumber(prompt):
    """
    Catches inputs by user for anything other than an integer.

    :param string prompt: The input provided by the user.
    :return int: The prompt converted to an int.
    """
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Pick a whole number, silly goose... try again.")
        else:
            return userInput

def promptCheck(prompt):
    """
    Checks for valid inputs at the menu prompt.

    :param string prompt: The input provided by the user.
    :return int: True if the input is valid, False otherwise.
    """
    arr = prompt.split(" ")
    if arr[0] not in ["r", "f", "q", "-c", "l"]:
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

def game_input():
    '''
    @pre Handles start game initial board parameters
    @post None
    @return height,width,mines tuple (ints)
    '''
    height = inputNumber("Enter the height of the board: ")
    while height > 24 or height < 2:
        height = inputNumber("Please enter a height between 2 and 24: ")

    width = inputNumber("Enter the width of the board: ")
    while width > 24 or width < 2:
        width = inputNumber("Please enter a width between 2 and 24: ")

    mines = inputNumber("Enter the number of mines: ")
    while mines >= height*width or mines <= 0:
        mines = inputNumber(f"Please use from 1 to {height*width - 1} mines: ")

    #add bounds checking

    return height, width, mines

def click(board, row, column, action):
    """
    Selects Cell to perform intended action on.

    :param Board board: The current Board object.
    :param int row: The row within the grid.
    :param int column: The column within the grid.
    :param string action: The action to perform on the Cell.
    :return bool: True if the user selects a bomb, False otherwise.
    """
    if action == "r":
        if board.grid[row][column].isBomb:
            return True
        elif board.grid[row][column].isFlagged:
            print("You can't reveal a flagged square. Please remove the flag and try again.")
            return False
        else:
            spread(board, row, column)
            return False
    elif action == "f":
        if board.grid[row][column].isRevealed:
            print("You cannot flag an space that's already revealed.")
        elif board.grid[row][column].isFlagged:
            board.flagCount -= 1
            board.grid[row][column].isFlagged = False
        else:
            if board.flagCount == board.mines:
                print("You cannot use more flags than bombs... remove a flag to place another;\n"
                      "place a flag on a square that has a flag in order to remove it.")
            else:
                board.flagCount += 1
                board.grid[row][column].isFlagged = True
        return False

def spread(board, row, column):
    """
    Recursively reveals adjacent Cells if they are empty.

    :param Board board: The current Board object.
    :param int row: The row within the grid.
    :param int column: The column within the grid.
    """
    if (board.grid[row][column].adj > 0 or board.grid[row][column].isRevealed):
        board.grid[row][column].isRevealed = True
    else:
        board.grid[row][column].isRevealed = True
        if row-1 >= 0:
            spread(board, row-1, column)
        if row+1 < board.height:
            spread(board, row+1, column)
        if column-1 >= 0:
            spread(board, row, column-1)
        if column+1 < board.width:
            spread(board, row, column+1)

def run_singleplayer():
    """
    Prompts the user for board size and number of mines, then runs the game.

    :return None:
    """

    height,width,mines = game_input()

    board = Board(height, width, mines)
    timeTaken = Time()
    show(board)
    leaders = Leaderboard('leaderboard.txt')

    lose = False
    flaggedBombCount = 0

    #begin game loop
    while not lose and flaggedBombCount != board.mines:
        choice = input("MENU:\n Reveal Square: r x y\n Add or Remove Flag: f x y\n Quit: q\n Show Leaderboard: l\n <Prompt>: ").lower() #TODO discuss possible prompts, like turn counter
        if promptCheck(choice):
            action = choice.split()[0]

            if action == "-c":
                cheatMode(board)

            if action == "r" or action == "f":
                column, row = int(choice.split()[1]), int(choice.split()[2])

                if column >= width or column < 0:
                    print ("Out of bounds x coordinate!")
                    while True:
                        try:
                            column = int(input("x: "))
                            while column >= width or column < 0:
                                column = int(input("Out of bounds! x: "))
                            break
                        except ValueError:
                            print ("Invalid input!")

                if row >= height or row < 0:
                    print ("Out of bounds y coordinate!")
                    while True:
                        try:
                            row = int(input("y: "))
                            while row >= height or row < 0:
                                row = int(input("Out of bounds! y: "))
                            break
                        except ValueError:
                            print ("Invalid input!")

                lose = click(board, row, column, action)
                if board.grid[row][column].isBomb and board.grid[row][column].isFlagged:
                        flaggedBombCount += 1
                show(board)
            elif action == "q":
                break
            elif action == "l":
                leaders.get_leaderboard()
                input("Press Enter to return to game...")




        else:
            print("Invalid command. Pick a whole number, silly goose... try again.")
    timeTaken.game_over_time()
    if lose:
        print("Bomb detonated! You need more practice, young grasshopper.")
        show(board, True)

    elif choice == "q":
        print("Thank you for playing... come again!")
    else:
        print("*Mario Voice* You are the weiner!")
        score = int(float(board.calculate_3bv()/timeTaken.show_total()))
        print(score)
        leaders.add_entry(score)

def run_coop():
    """
    client side version of coop multiplayer
    """
    lose = False
    flaggedBombCount = 0

    #begin game loop
    while not lose and flaggedBombCount != board.mines:
        choice = input("MENU:\n Reveal Square: r x y\n Add or Remove Flag: f x y\n Quit: q\n <Prompt>: ").lower() #TODO discuss possible prompts, like turn counter
        if promptCheck(choice):
            action = choice.split()[0]

            if action == "r" or action == "f":
                column, row = int(choice.split()[1]), int(choice.split()[2])

                if column >= width or column < 0:
                    print ("Out of bounds x coordinate!")
                    while True:
                        try:
                            column = int(input("x: "))
                            while column >= width or column < 0:
                                column = int(input("Out of bounds! x: "))
                            break
                        except ValueError:
                            print ("Invalid input!")

                if row >= height or row < 0:
                    print ("Out of bounds y coordinate!")
                    while True:
                        try:
                            row = int(input("y: "))
                            while row >= height or row < 0:
                                row = int(input("Out of bounds! y: "))
                            break
                        except ValueError:
                            print ("Invalid input!")

                lose = click(board, row, column, action)
                if board.grid[row][column].isBomb and board.grid[row][column].isFlagged:
                        flaggedBombCount += 1
                show(board)
            elif action == "q":
                break
        else:
            print("Invalid command. Pick a whole number, silly goose... try again.")

    if lose:
        print("Bomb detonated! You need more practice, young grasshopper.")
        show(board, True)
    elif choice == "q":
        print("Thank you for playing... come again!")
    else:
        print("*Mario Voice* You are the weiner!")


'''
def end_game()
    player won
        submit score
        try again

    player lost
        try again
'''
