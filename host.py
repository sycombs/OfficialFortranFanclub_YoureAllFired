'''
host.py
'''
from GameLogic import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
#below allows us to reuse a socket within an amount of time
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',SERVER_PORT))

if __name__ == "__main__":
    '''
    Starts UI, complete with input checking and auto server starting
    '''
    mode = 0
    print("\nWelcome to Minesweeper!\n")
    while mode < 1 or mode > 3:
        mode = inputNumber("\nPlease select a mode:\n\nSingle Player: 1\nCo-op: 2\nVersus: 3\n\nYour input: ")
    if mode == 1:
        height,width,mines = game_input()

        board = Board(height, width, mines)

        run_singleplayer(board)
    elif mode == 2:
        response = False
        print("\nYour IP: " + gethostbyname(gethostname()))
        print("\nCo-op selected! Waiting for Player 2...\n")
        while not response:
            try:
                response, clientAddress = serverSocket.recvfrom(2048 * 2 * 2)
            except:
                print ("Something went wrong")
        print("Player 2 has connected!")
        send_comm('coop',serverSocket,clientAddress)
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
        run_coop(serverSocket, clientAddress, True, board)

    elif mode == 3:
        print("\nYour IP: " + gethostbyname(gethostname()))
        response = False
        print("\nVersus selected! Waiting for Player 2...\n")
        while not response:
            try:
                response, clientAddress = serverSocket.recvfrom(2048 * 2 * 2)
            except:
                print ("Something went wrong")
        print("Player 2 has connected!")
        send_comm('vs',serverSocket,clientAddress)
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
        run_versus(serverSocket, clientAddress, board)
