from gameSet import gameSet

class game:
    def __init__(self, gameID: int):
        self.valid: bool
        self.gameID = gameID
        self.balls: gameSet

    def add(self, red: int, green: int, blue: int):
        self.balls.red += red
        self.balls.green += green
        self.balls.blue += blue
