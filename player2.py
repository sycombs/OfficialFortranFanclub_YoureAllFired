'''
player2.py
initiates client connection to host
'''

from GameLogic import *
from OFF_Network import *
#create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)


'''


NEW ADDRESS GETS ENTERED HERE


'''


#send initial connection
mode = False
while mode == False:
    servAddr = input("Enter Server Address: ")
    LAN_SERVER_INFO = (servAddr, SERVER_PORT)
    try:
        mode = send_comm("True", clientSocket, LAN_SERVER_INFO,True)
        mode = mode.decode()
    except Exception as e:
        print ("\nAddress incorrect! (Get it from player 1!)\n")
        mode = False
data = 0
print("Waiting for player 1 to input board parameters...")
while data == 0:
    data, address = clientSocket.recvfrom(2048*2*2)
data = deserialize_data(data)
height,width,mines = data['height'],data['width'],data['mines']
#print (height,width,mines)
board = Board(height,width,mines)
for r in range(0,height):
    for c in range(0, width):
        tempCell = send_comm("True",clientSocket,LAN_SERVER_INFO,True)
        tempCell.decode()
        tempCell = deserialize_data(tempCell)
        newCell  = convert_dictionary_to_cell(tempCell)
        board.brute_force(newCell, r, c)
send_comm("False", clientSocket, LAN_SERVER_INFO)
if mode == 'coop':
    run_coop(clientSocket,LAN_SERVER_INFO,False,board)
elif mode == 'vs':
    run_versus(clientSocket,LAN_SERVER_INFO,board)
