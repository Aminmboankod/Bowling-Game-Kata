
class Game:
    
    

    def strike(card):
        for roll in card:
            if roll == "X":
                return 10
    
    def spare(card, next_roll):
        for roll in card:
            if roll == "/":
                return 10+(next_roll)

    def noPins():
        pass

    def normalLauch():
        pass

game = Game()
throw = Game()
next_roll = Game()
