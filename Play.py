from Board import Board
from colorama import Fore, Style
import time
from GameLogic import *
import player
import pickle

if __name__ == "__main__":
    #prompt for player input
    mode = 0
    print("\nWelcome to Minesweeper!\n")
    while mode < 1 or mode > 3:
        mode = inputNumber("\nPlease select a mode:\n\nSingle Player: 1\nCo-op: 2\nVersus: 3\n\nYour input: ")
    if mode == 1:
        run_singleplayer()
    elif mode == 2:
        p = player.Player()
        if p.send_player_state() == b'inp':
            #b'inp' means this is first player so set id to 1
            p.playerData['ID'] = 1
            #ask for board input (only first player)
            board_tuple = game_input()
            #msg in playerdata is used to convey any info, could add more elements
            p.playerData['msg'] = " ".join(str(x) for x in board_tuple)
            '''
            TODO Fix below
            The below is an attempt to handle multiple pickle packets

            data = []
            while True:
                packet = s.recv(4096)
                if not packet: break
                data.append(packet)
            data_arr = pickle.loads(b"".join(data))
            '''
            board = pickle.loads(p.send_player_state())
            show(board)

        #print("Only single player is working right now")
    elif mode == 3:
        print("Only single player is working right now")

    #if co-op: run co-op logic & send & receive player data
    #if versus: run versus logic & send & receive player data
