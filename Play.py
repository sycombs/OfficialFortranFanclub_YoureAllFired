#import Map

def run():

    height = input("Enter the height of the board:")
    width = input("Enter the width of the board:")
    mines = input("Enter the number of mines:")
    #board = Map(height, width, mines)

    lose = False
    while not lose:
        action = input("What would you like to do? Enter 'r' to reveal or 'f' to flag:")
        if action == "r": text = "reveal"
        else: text = "flag"
        row = input(f"For the cell you would like to {text}, enter row:")
        column = input(f"For the cell you would like to {text}, enter column:")

        lose = click(row, column, action)

def click(row, column, action):
    return True

run()