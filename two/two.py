from game import game
from gameSet import gameSet

validationCriteria = gameSet(12, 13, 14)

def sumValidGames(games: list[game]) -> int:
    sum: int
    for game in games:
        if game.valid:
            sum += game.gameID
    return sum


def valid(game: game) -> bool:
    if game.balls.red > validationCriteria.red:
        return False
    elif game.balls.green > validationCriteria.green:
        return False
    elif game.balls.blue > validationCriteria.blue:
        return False
    
    return True

def validateGames(games: list[game]) -> list:
    for game in games:
        if valid(game):
            game.valid = True
        else:
            game.valid = False
    return games

def retrieveID() -> int:

    return

def processSets(setString: str) -> gameSet:
    set: gameSet


def processInput(rawInput: list[str]) -> list[game]:
    gameID = retrieveID()

    return 

def readInput(filePath: str) -> list[str]:
    file = open(filePath,'r')
    input = file.readlines()

    return input

def main():
    testMode = True
    if testMode:
        rawInput = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
    else:
        rawInput = readInput("two/input.txt")
    cleanGames = processInput(rawInput)
    validGames = validateGames()
    result = sumValidGames(validGames)
    print(result)
    return 0
    
main()