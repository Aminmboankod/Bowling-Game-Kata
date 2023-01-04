
class Game:

    def __init__(self):
        self.bonus = 0
        self.score = 0 

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


    def totalScore(self, card):
        index = -1
        for roll in card:
            index += 1
            previousRoll = card[card.find(roll)-1]
            nextRoll = card[card.find(roll)+1]
            nextOf_nextRoll = card[card.find(roll)+2]   
            if roll == "/":
                self.score += ((self.scoreFrame(nextRoll)) - (self.scoreFrame(previousRoll)))
            if roll == "X":
                if index == 9:
                    self.score -= (((self.scoreFrame(nextRoll)) + (self.scoreFrame(nextOf_nextRoll))) * 3)
                self.score += (self.scoreFrame(nextRoll)) + (self.scoreFrame(nextOf_nextRoll))
            self.score += self.scoreFrame(roll)
        return self.score

