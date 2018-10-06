'''
versuslogic.py
handles communication between clients and server
called after selecting versus option in play
'''

#def __init__(self):
#   player_count = 0
#   on startup wait for first client (receivefrom...)
#   on player connection (receiving player data)
#       player_count++
#       player_id = player_count
#       prompt player 1 for board input
#       receive tuple (height, width, mines)
#       board = Board(height,width,mines)

#   wait for client 2 (receivefrom...)
#   on player connection (receiving player data)
#       player_count++
#       player_id = player_count
#       relay game parameters to player 2
#       time.sleep(1)

#def game_loop()
#    send board data to both players
#
#    start game loop
#    each player plays esentially a single player game
#    sends game loss/win to server
#    while nobody has won/lost:
#        wait for client to send a win/loss
#        on receipt of win/loss:
#            tell other client they lost/won
#        close server
#
