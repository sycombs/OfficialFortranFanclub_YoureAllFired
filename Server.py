"""@package docstring
Server.py contains all of the game server functionality. A server should
    1) Be created
    2) Listen for incoming messages
    3) Interpret messages and call other code as necessary

Server.py should not be used to run a server, any instances of a server
should be created in Play.py . Server.py does not handle game logic either, it
only facilitates the communication between the client (where the user interacts)
and the server (where the game specific code is handled).

We may not run a pure client-server model so keep that in mind when moving
code out of this file... like the server loop
"""
