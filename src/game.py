class Game:

    def __init__(self, card):
        self.bonus = ""
        self.score = 0
        self.frame = 0
        self.rolls = 0
        self.index = -1
        self.lastRoll = 0
        self.card = card

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
                self.scoreRoll(roll)
                self.rolls += 1
                if self.rolls == 2:
                    self.frame += 1
                    self.rolls = 0
            if roll == "-":
                self.scoreRoll(roll)
                self.rolls += 1
                if self.rolls == 2:
                    self.frame += 1
                    self.rolls = 0
            if roll == "X":
                self.scoreRoll(roll)
                self.scoreBonus(self.card[self.index+1:self.index+3])
                self.frame += 1
            if roll =="/":
                self.scoreRoll(roll)
                self.scoreBonus(self.card[self.index+1])
                self.frame += 1
                self.rolls = 0
            if self.frame == 9:
                self.scoreRoll(self.card[self.index+1:])
                break
        return self.score

