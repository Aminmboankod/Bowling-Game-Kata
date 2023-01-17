from scoreCard import ScoreCard

class Game:

    def __init__(self):
        self.total = 0

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total
    
    def roll(self, pins):
        self.setTotal(self.getTotal() + ScoreCard.getLaunchesValue(pins))