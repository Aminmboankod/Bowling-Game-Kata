
class Game:

    def __init__(self):
        self.score = 0

        
    def strike(self):
        self.score += 10 + self.bonus()

    def spare(self):
        self.score += 10 + self.bonus()

    @staticmethod
    def noPins():
        return 0

    def launch(self, card):
        self.score += int(card)

    def bonus(self, frameScore):
        specialBonus = 0
        for frame in frameScore:
            specialBonus += self.scoreFrame(frame)
        return specialBonus

    @staticmethod
    def scoreFrame(frame):
        if frame == "X":
            return 10
        if frame == "/":
            return 10
        if frame == "-":
            return 0
        if frame.isdigit():
            return int(frame)

        

    def totalScore(self, card):
        index = -1
        lastRoll = 0
        if card[-2] == "/":
                self.score -= int(card[-1])
        for roll in card:
            index += 1
            if roll == "X":
                if index == 9:
                    self.score
                else:
                    self.score += self.scoreFrame(roll) + self.bonus((card[index+1:index+3]))
            if roll == "/":
                self.score += self.scoreFrame(roll) + self.bonus((card[index+1]))-lastRoll
            if roll == "-":
                continue
            if roll.isdigit():
                self.score += int(roll)
                lastRoll = int(roll)
                       
        return self.score
