"""@package docstring
Leaderboard.py is in charge of creating and managing a leaderboard text file. Currently allows adding, clearing, printing, and searching across the leaderboard.
"""
class Leaderboard:
    #score variable
    def __init__(self, fname):
        """
        Constructs a leaderboard object that is linked to the text file of fname
        :param fname: The name of the leaderboard text file.
        :return None
        """
        self.fileName = fname

    def get_leaderboard(self, number):
        """
        Prints out the top x entries on the leaderboard, where x is the number passed in.
        :param number: The number of spaces to print from the leaderboard
        :return None
        """
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

    def get_score(self, number):
        """
        Returns the score of the individual in place x of the leaderboard, where x is number
        :param number: The place of the score that we want to find.
        :return score of that place in the leaderboard
        """
        scores = 0
        players = []
        with open(self.fileName, 'r') as self.file:
            for line in self.file:
                currentLine = line[:-1]
                players.append(currentLine)
        for items in players:
            scores = int(items[14:len(items)-1])
            number-=1
            if number==0:
                return scores
        return scores

    def sort_leaderboard(self):
        """Sorts the leaderboard so that the smallest number is at the bottom, while the largest number is at the top.
        :param none
        :return none
        """
        #sorts Leaderboard
        players = []
        with open(self.fileName, 'r') as self.file:
            for line in self.file:
                currentLine = line[:-1]
                players.append(currentLine)
        def player_key(s):
            return int(float(s[14:len(s)-1]))
        players2=sorted(players, key=player_key, reverse=True)
        with open(self.fileName, 'w') as self.file:
            for items in players2:
                items=items+'\n'
                self.file.write(items)

    def add_entry(self, score):
        """
        Takes in the score, and then asks for the individuals name.  After which saves the name and score to the leaderboard text file.
        :param score: The score of the individual who would be
        :return None
        """
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
        """
        Removes all of the names on the leaderboard.
        :param none
        :return None
        """
        #clear leaderboard
        with open(self.fileName, 'w') as self.file:
            self.file.write('')
