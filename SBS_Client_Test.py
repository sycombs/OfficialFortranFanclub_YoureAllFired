from SideBySide_Play import *

# Player 1 starts the game and enters parameters
p1 = NetPlayer()

send

# Player 2 connects to Player 1

# Once both players are ready we kill the connection between them

# Both players send their boards to the server which then sends each player
# the other player's board

# Send self board to server
# Receive enemy board from server

'''
We need a server so that one player can't hold the other one up
by not doing anything
'''

# Get the other player's board

# Game play loop
    # Make a move
    # If it's good, send it to the server and request for the buffer
    # Run the other player's buffer
    # Display both boards

    # If you get a lose flag, you lose!

    # If you win: Send win flag to server

    # If you lose: Send lose flag and new board to the server


# Draw two boards at once
# def draw_two_boards()
