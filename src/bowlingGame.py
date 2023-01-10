class Game:

    def __init__(self, card):
        self.score = 0
        self.frame = 0
        self.rolls = 0
        self.index = -1
        self.lastRoll = 0
        self.card = card


    # Métodos de cálculo de puntuación y bonus
    def scoreRoll(self, card):
        for roll in card:
            if roll.isdigit():
                self.lastRoll = int(roll)
                self.score += int(roll)
                continue
            if roll == "-":
                self.lastRoll = 0
                self.score += 0
                continue
            if roll == "X":
                self.score += 10
                continue
            if roll == "/":
                self.score -= self.lastRoll
                self.lastRoll = 0
                self.score += 10

    def scoreBonus(self, bonus):
        for roll in bonus:
            self.scoreRoll(roll)

    def totalScore(self):
        for roll in self.card:
            self.index += 1
            if roll.isdigit():
                self.num(roll)
            if roll == "-":
                self.null(roll)
            if roll == "X":
                self.strike(roll)
            if roll =="/":
                self.spare(roll)
            if self.frame == 9:
                self.scoreRoll(self.card[self.index+1:])
                break
        return self.score
    

    # launches methods
    def strike(self, roll):
        self.scoreRoll(roll)
        self.scoreBonus(self.card[self.index+1:self.index+3])
        self.frame += 1 

    def spare(self, roll):
        self.scoreRoll(roll)
        self.scoreBonus(self.card[self.index+1])
        self.setFrame()

    def null(self, roll):
        self.scoreRoll(roll)
        self.rolls += 1
        self.setRoll()

    def num(self, roll):
        self.scoreRoll(roll)
        self.rolls += 1
        self.setRoll()


    # set frames and rolls
    def setFrame(self):
        self.frame += 1
        self.rolls = 0

    def setRoll(self):
        if self.rolls == 2:
            self.setFrame()        
