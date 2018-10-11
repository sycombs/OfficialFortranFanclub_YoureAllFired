"""@package docstring
Time.py is in charge of comparing the amount of time it takes to complete a task, along with some other functions regarding timing.
"""
import time
class Time:

    def __init__(self):
        """
        Constructs a Time object with start time being time it is initiated
        :param none
        :return None
        """
        self.start = time.time()
        self.end = time.time()
        self.totalTime = self.totalTime = self.end-self.start
        self.turnStart = time.time()


    def game_over_time(self):
        """
        Changes the end time to when this function is called, and calculates the time difference
        :param none
        :return None
        """
        self.end = time.time()
        self.totalTime = self.end-self.start


    def show_total(self):
        """
        Returns the total time it took to complete from beginning to end
        :param none
        :return TotalTime, the time difference between start and end
        """
        return self.totalTime

    def compare_time(self, other):
        """
        None
        :param Time Other: Prints the larger time between itself and other
        :return None
        """
        if self.totalTime>other.showTotal:
            print("You Win!")
        elif self.totalTime<other.showTotal:
            print("You Lose...")
        else:
            print("It's a draw?")

    def turn_start(self):
        """
        Calculates a turn time beginning to measure the time taken between turns.
        :param none
        :return none
        """
        self.turnStart=time.time()

    def time_limit(self, timeLimit):
        """
        Calculates a turn time beginning to measure the time taken between turns.
        :param timeLimit: the time limit to check the turnStart time difference to.
        :return True if still their turn, false if not
        """
        if (self.turnStart + timeLimit) >= time.time():
            return True
        else:
            return False

    def time_delay(self, timeLimit):
        """
        makes the computer sleep from a certain amount of time
        :param timeLimit: the amount of time to sleep the computer for
        :return none
        """
        time.sleep(timeLimit)
    # def countDown(hour, min, sec):
    #     self.min, self.sec = divmod(sec, 60)
    #     self.hour, self.min = divmod(min, 60)
    #     timedisplay = '{:02d}{:02d}:{02d}'.format(hour, min, sec)
    #     print(timedisplay, end='\r')
    #     time.sleep(1)
    #     sec -= 1
