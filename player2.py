'''
player2.py
'''

from GameLogic import *
from OFF_Network import *
#create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#send initial connection

responseData = send_comm("True", clientSocket, SERVER_INFO,True)
responseData.decode()
data = deserialize_data(responseData)
height,width,mines = data['height'],data['width'],data['mines']
print (height,width,mines)
board = Board(height,width,mines)
for r in range(0,height):
    for c in range(0, width):
        tempCell = send_comm("True",clientSocket,SERVER_INFO,True)
        tempCell.decode()
        tempCell = deserialize_data(tempCell)
        newCell  = convert_dictionary_to_cell(tempCell)
        board.brute_force(newCell, r, c)
send_comm("False", clientSocket, SERVER_INFO)
board.displayBoard()
run_coop(clientSocket,SERVER_INFO,False,board)
