from src.scoreCard import ScoreCard

class Game:

    def __init__(self):
        self.total = 0
        self.ScoreCard = ScoreCard()

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total
    
    def roll(self, pins):
        self.setTotal(self.getTotal() + self.ScoreCard.getLaunchesValue(pins))