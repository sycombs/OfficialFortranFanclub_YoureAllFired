from GameLogic import *

if __name__ == "__main__":
    board = Board(0,0,0)
    mode = 0
    print("\nWelcome to Minesweeper!\n")
    while mode < 1 or mode > 3:
        mode = inputNumber("\nPlease select a mode:\n\nSingle Player: 1\nCo-op: 2\nVersus: 3\n\nYour input: ")
    if mode == 1:
        run_singleplayer()
    elif mode == 2:
        #try:
            p = player.Player()
            board = mult_start_inp(p, board)
        #except:
        #    print("Server needs to be online first! (run Server.py from another terminal)")
    elif mode == 3:
        print("Only single player is working right now")

    #if co-op: run co-op logic & send & receive player data
    #if versus: run versus logic & send & receive player data
