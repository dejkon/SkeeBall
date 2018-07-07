

class Player:

    def __init__ (self, player):
        self.player = player
        self.score = 0

    def calcScore (self, pointsScored):
        self.score += pointsScored
        return self.score
