class Player:
    def __init__(self, letter):
        self.letter = letter

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

class Random(Player):
    def __init__(self, letter):
        super().__init__(letter)