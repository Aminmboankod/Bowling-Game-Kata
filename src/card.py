
class Card:

    card = {"frames" :{
    {1:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {2:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {3:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {4:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {5:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {6:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {7:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {8:{{"roll":{{str},{str}}},
        {"score":{int}}}}, 
    {9:{{"roll":{{str},{str}}},
        {"score":{int}}}},
    {10:{{"roll":{{str},{str}}},
        {"score":{int}}}}
        }
    }

    def __init__(self, card, frame, roll):
        self.card = card
        self.frame = frame
        self.roll = roll
        self.score = 0

    # ----- Get Methods -----
    def getFrames(self, frame):
        return self.card["frames"[frame]]

    def getRoll(self):
        return card["frames"[self.getFrames():["roll"]]]

    def getscore():
        pass
    
    # ----- Set Methods -----  
    def setFrames(self, frame):
        self.frame = frame
    
    def setRoll(self, roll):
        self.roll = roll

    def setScore(self, frame):
        pins = self.getFrames(frame)[self.getRoll()]
        self.score = 0
        for roll in pins:
            self.score += roll
        return self.score

    
