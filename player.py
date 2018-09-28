from socket import *
import pickle


serverName = '127.0.0.1'
serverPort = 12000

serverInfo = (serverName, serverPort)

class Player:
    def __init__(self):
        self.playerID = 0

    def sendA(self, basicData):
        # Assuming we have a string for the data, use this for now
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.sendto(basicData.encode(), serverInfo)
        #clientSocket.sendto(pNum, (self.serverName, self.serverPort))

        # Process response from the server
        #serverResponse, serverAddress = clientSocket.recvfrom(2048)
        #print(serverResponse.decode())
        #clientSocket.close()

    def sendB(self, complexData):
        # complexData includes functions and objects
        cData = pickle.dumps(complexData)

        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.sendto(cData, serverInfo)

        # Process response from the server
        #serverResponse, serverAddress = clientSocket.recvfrom(2048)
        #print(serverResponse.decode())
        #clientSocket.close()

    def pFunc(self):
        print('This is being printed by an external function')
