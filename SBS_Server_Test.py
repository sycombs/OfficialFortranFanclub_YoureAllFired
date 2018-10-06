from SideBySide_Server import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', SERVER_PORT))

print("Test Server")
while True:
    message, clientSocket = serverSocket.recvfrom(2048)
    respond_to_message(message, clientSocket)
