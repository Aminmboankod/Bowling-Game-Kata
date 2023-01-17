
class ScoreCard:

    def __init__(self, scoreCard= ""):
        self.scoreCard = scoreCard
        self.totalScore = 0
        self. firstRoll = True
        self.spare = False
        self.strike = False
        self.firstRollPins = 0
        self.doubleStrike = False
        self.rolls = len(scoreCard)
        self.launches = "-123456789X/"

    def getScoreCard(self):
        return self.scoreCard

    def getTotalScore(self):
        return self.totalScore

    def setTotalScore(self, total):
        self.totalScore = total

    def isSpare(self):
        return self.spare

    def setSpare(self, spare):
        self.spare = spare
    
    def isFirstRoll(self):
        return self.firstRoll
    
    def setFirstRoll(self, value):
        self.firstRoll = value
    
    def setFirstRollPins(self, pins):
        self.firstRollPins = pins
    
    def getFirstRollPins(self):
        return self.firstRollPins
    
    def setStrike(self, strike):
        self.strike  = strike
    
    def isStrike(self):
        return self.strike
    
    def setDouble(self, value):
        self.doubleStrike = value
    
    def isDouble(self):
        return self.doubleStrike

    def isExtraRoll(self):
        return self.rolls <= 2
    
    def isLastExtraRoll(self):
        return self.rolls ==1
    
    def isLastFrame(self):
        return self.rolls <= 3

    def getLaunchesValue(self, launch):
        return self.launches.find(launch)

    def calculateScore(self):
        for i in range(len(self.getScoreCard())):
            pin = self.getScoreCard([i])
            self.roll(pin)
        
    def roll(self, pins):
        if pins =="X":
            if self.isStrike() and  not self.isExtraRoll():
                self.setTotalScore(self.getTotalScore() + self.getFirstRollPins())

            elif self.isDouble() and not self.isLastExtraRoll():
                self.setTotalScore(self.getTotalScore() + self.getFirstRollPins())
                
            elif self.isStrike() and not self.isLastFrame():
                self.setDouble(True)
                
            self.setTotalScore(self.getTotalScore() + self.getSymbolValue(pins))
            self.setStrike(True)
            self.setFirstRoll(True)

        elif self.isFirstRoll():
            self.setFirstRollPins(self.getSymbolValue(pins))
            self.setFirstRoll(False)
			
            if self.isStrike() and not self.isExtraRoll():
                self.setTotalScore(self.getTotalScore() + self.getFirstRollPins())
            
            elif self.isDouble() and not self.isLastExtraRoll():
                self.setTotalScore(self.getTotalScore() + self.getFirstRollPins())
                
            self.setStrike(False)
            self.setDouble(False)
        
        elif self.isSpare():
                self.setTotalScore(self.getTotalScore() + self.getFirstRollPins())
                
        elif pins == '/':
            self.setTotalScore(self.getTotalScore() + 10)
            self.setSpare(True)
            if self.isStrike():
                self.setTotalScore(self.getTotalScore() + 5)
                
            self.setStrike(False)
            self.setFirstRoll(True)
            
        else:
            self.setTotalScore(self.getTotalScore() + self.getFirstRollPins() + self.getLaunchesValue(pins))
            if self.isStrike():
                self.setTotalScore(self.getTotalScore() + self.getLaunchesValue(pins))
                
            self.setFirstRoll(True)
            self.setSpare(False)
            self.setStrike(False)
        self.rolls-= 1
