class Leaderboard:
    #score variable
    def __init__(self):
        self.fileName = 'leaderboard.txt'

    #def get_leaderboard(self):
        #return top 10...20 scores

    def sort_leaderboard(self):
        #sorts Leaderboard
        players = []
        with open(self.fileName, 'r') as self.file:
            for line in self.file:
                currentLine = line[:-1]
                players.append(currentLine)
        def player_key(s):
            return int(s[14:len(s)-1])
        players2=sorted(players, key=player_key)
        with open(self.fileName, 'w') as self.file:
            for items in players2:
                items=items+'\n'
                self.file.write(items)

    def add_entry(self, score):
        #add score to leaderboard
        self.name= input("Please enter your Name (9 letters max): ")
        while len(self.name)>9:
            self.name = input("Invalid entry, too many letters.  Make sure it is only 9 letters.\nPlease enter your name (9 letters max): ")
        while len(self.name)<9:
            self.name = self.name + ' '
        entry=(self.name, score)
        values=str(entry)+'\n'
        with open(self.fileName, 'a') as self.file:
            self.file.write(values)
        self.sort_leaderboard()
    #def clear(self):
        #clear leaderboard
