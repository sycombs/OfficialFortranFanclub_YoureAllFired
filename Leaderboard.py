class Leaderboard:
    #score variable
    def __init__(self, fname):
        self.fileName = fname

    def get_leaderboard(self, number):
        #return top 10...20 scores
        print('Players  ', '\t', 'Scores')
        players = []
        with open(self.fileName, 'r') as self.file:
            for line in self.file:
                currentLine = line[:-1]
                players.append(currentLine)
        for items in players:
            print(items[2:10], '\t', items[14:len(items)-1])
            number-=1
            if number==0:
                return


    def sort_leaderboard(self):
        #sorts Leaderboard
        players = []
        with open(self.fileName, 'r') as self.file:
            for line in self.file:
                currentLine = line[:-1]
                players.append(currentLine)
        def player_key(s):
            return int(float(s[14:len(s)-1]))
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

    def clear(self):
        #clear leaderboard
        with open(self.fileName, 'w') as self.file:
            self.file.write('')
