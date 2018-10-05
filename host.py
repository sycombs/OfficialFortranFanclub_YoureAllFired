'''
host.py
'''
from GameLogic import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
#below allows us to reuse a socket within an amount of time
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',SERVER_PORT))

if __name__ == "__main__":
    mode = 0
    print("\nWelcome to Minesweeper!\n")
    while mode < 1 or mode > 3:
        mode = inputNumber("\nPlease select a mode:\n\nSingle Player: 1\nCo-op: 2\nVersus: 3\n\nYour input: ")
    if mode == 1:
        run_singleplayer()
    elif mode == 2:
        response = False
        print("\nCo-op selected! Waiting for Player 2...\n")
        while not response:
            try:
                response, clientAddress = serverSocket.recvfrom(2048 * 2 * 2)
            except:
                print ("Something went wrong")
        print("we did it")
        height,width,mines = game_input()
        data_dict = {
            'height' : height,
            'width' : width,
            'mines' : mines
        }
        data = serialize_data(data_dict)
        board = Board(height, width, mines)
        send_comm(data, serverSocket,clientAddress)
        for r in range(0, board.height):
            for c in range(0, board.width):
                tempCell = convert_cell_to_dictionary(board.grid[r][c])
                response = send_comm(serialize_data(tempCell), serverSocket, clientAddress,True)
        board.displayBoard()
        run_coop(serverSocket, clientAddress, True, board)
        #we're here because we got a response
        #receive clientaddress
        #run_coop(hostSocket,clientAddress,board)

    elif mode == 3:
        print("Only single player is working right now")
