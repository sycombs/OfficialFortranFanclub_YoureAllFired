from Board import Board
from colorama import Fore, Style
import time
from GameLogic import *

def run():
    """
    Prompts the user for board size and number of mines, then runs the game.

    :return None:
    """

    height,width,mines = game_input()

    board = Board(height, width, mines)
    show(board)

    lose = False
    flaggedBombCount = 0

    #begin game loop
    while not lose and flaggedBombCount != board.mines:
        choice = input("MENU:\n Reveal Square: r x y\n Add or Remove Flag: f x y\n Quit: q\n <Prompt>: ").lower() #TODO discuss possible prompts, like turn counter
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
        else:
            print("Invalid command. Pick a whole number, silly goose... try again.")

    if lose:
        print("Bomb detonated! You need more practice, young grasshopper.")
        show(board, True)
    elif choice == "q":
        print("Thank you for playing... come again!")
    else:
        print("*Mario Voice* You are the weiner!")

if __name__ == "__main__":
    #prompt for player input
    mode = 0
    print("\nWelcome to Minesweeper!\n")
    while mode < 1 or mode > 3:
        mode = inputNumber("\nPlease select a mode:\n\nSingle Player: 1\nCo-op: 2\nVersus: 3\n\nYour input: ")
    if mode == 1:
        run()
    elif mode == 2:
        print("Only single player is working right now")
    elif mode == 3:
        print("Only single player is working right now")

    #if co-op: run co-op logic & send & receive player data
    #if versus: run versus logic & send & receive player data
