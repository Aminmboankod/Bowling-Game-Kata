
class Game:

    def __init__(self, card):
        self.bonus = 0
        self.score = 0
        self.card = card

    # Comprueba tirada devuelve True si es strike
    @staticmethod
    def strike(roll):
        if roll == "X":
            return True

    # Comprueba tirada devuelve True si es spare
    @staticmethod
    def spare(roll):
        if roll == "/":
            return True

    # Comprueba tirada devuelve True si no se ha tirado ningún bolo 
    @staticmethod
    def noPins(roll):
        if roll == "-":
            return True

    # Comprueba tirada devuelve True si es una tirada sin bonus
    @staticmethod
    def launch(roll):
        if roll.isdigit():
            return True
        
    # Creamos método que asigna puntuación en función del tipo de tirada
    def scoreFrame(self, roll):
        if self.strike(roll) == True:
            return 10
        if self.spare(roll) == True:
            return 10
        if self.noPins(roll) == True:
            return 0
        else:
            return int(roll)
    
    def lastBonus(self):
        if self.card[-3] == "X":
            return True
            
        if self.card[-2] == "/":
            return True

    def bonusMatch(self):
        if self.card[-3] == "X":
            self.card = self.card[:-3]
            self.bonus += ((self.scoreFrame(self.card[-1])) + (self.scoreFrame(self.card[-2])) + (self.scoreFrame(self.card[-3])))
            return self.bonus

        if self.card[-2 == "/"]:
            self.card = self.card[:-2]
            self.bonus += ((self.scoreFrame(self.card[-1]))+(self.scoreFrame(self.card[-2])))
            return self.bonus




    def totalScore(self):
        if self.lastBonus() == True:
            self.score += self.bonusMatch()
        for roll in self.card:
            if roll == "/": 
                self.score += ((self.scoreFrame(self.card[self.card.find(roll)+1])) - (self.scoreFrame(self.card[self.card.find(roll)-1])))
            if roll == "X":
                self.score += (self.scoreFrame(self.card[self.card.find(roll)+1])) + (self.scoreFrame(self.card[self.card.find(roll)+2]))
            self.score += self.scoreFrame(roll)
            
        return self.score

