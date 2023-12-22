def processBuffer(word):
    if "one" in word:
        return "1"
    elif "two" in word:
        return "2"
    elif "three" in word:
        return "3"
    elif "four" in word:
        return "4"
    elif "five" in word:
        return "5"
    elif "six" in word:
        return "6"
    elif "seven" in word:
        return "7"
    elif "eight" in word:
        return "8"
    elif "nine" in word:
        return "9"
    else:
        return ""

def processLineNumber(lineNumber):
    if len(lineNumber) == 1:
            lineNumber += lineNumber
    elif len(lineNumber) > 2: 
            lineNumber = lineNumber[0] + lineNumber[-1]
    return lineNumber

def processInput(stringArray: list[str]):
    hiddenNumbers = []

    for line in stringArray:
        line = line.lower()
        lineNumber = ""
        wordBuffer = ""
        for character in line:
            # if it's number, then check the word buffer for any numbers, add any numbers from letters
            # add the number add it to line number
            if '0' <= character <= '9':
                numbersInLetters = processBuffer(wordBuffer)
                lineNumber += character
            # if it's a letter, add it to the buffer then check
            elif 'a' <= character <= 'z':
                wordBuffer += character
                number = processBuffer(wordBuffer)
                if number != "":
                    wordBuffer = ""
                    lineNumber += number

        lineNumber = processLineNumber(lineNumber)
        hiddenNumbers.append(int(lineNumber))

    return hiddenNumbers

def readInput(filePath):
    file = open(filePath,'r')
    input = file.readlines()

    return input

def main():
    testMode = False
    if testMode:
        bigArray = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    else: 
        bigArray = readInput("one/input.txt")
    hiddenNumbers = processInput(bigArray)
    result = sum(hiddenNumbers)
    print(result)
    return()

main