import time
class Time:
    def __init__(self):
        self.start = time.time()
        self.end = time.time()
        self.totalTime = self.totalTime = self.end-self.start
    def game_over_time(self):
        self.end = time.time()
        self.totalTime = self.end-self.start
    def show_total(self):
        return self.totalTime
    def compare_time(self, other):
        if self.totalTime>other.showTotal:
            print("You Win!")
        else if self.totalTime<other.showTotal:
            print("You Lose...")
        else:
            print("It's a draw?")
    def time_limit(self, timeLimit):
        if(self.start + timeLimit >= time.time())
        {
            return True;
        }
        else
        {
            return False
        }
    # def countDown(hour, min, sec):
    #     self.min, self.sec = divmod(sec, 60)
    #     self.hour, self.min = divmod(min, 60)
    #     timedisplay = '{:02d}{:02d}:{02d}'.format(hour, min, sec)
    #     print(timedisplay, end='\r')
    #     time.sleep(1)
    #     sec -= 1
