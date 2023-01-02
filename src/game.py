
class Game:
    
    
    @staticmethod
    def strike(card):
        for roll in card:
            if roll == "X":
                return 10

    @staticmethod
    def spare(card, next_roll):
        for roll in card:
            if roll == "/":
                return 10+(next_roll)

    @staticmethod
    def noPins(card):
        for roll in card:
            if roll == "-":
                return 0

    @staticmethod
    def Launch(card):
        score = 0
        for roll in card:
            score += int(roll)
        return score


game = Game()
throw = Game()
next_roll = Game()
