from random import randint
from prettytable import PrettyTable
import sys

answer = 0
chance = 0
minNum = 0
maxNum = 100
pastGuesses = []

def randNum(min, max):
    return randint(min, max)

def guessDistance(a, g):
    d = a - g
    return abs(d)
    
def incChance():
    global chance
    chance += 1

def logGuess(g, d):
    global pastGuesses
    global chance
    pastGuesses.append([chance, g, d])

def incorrectGuess(g, d, m):
    global answer
    global minNum
    global maxNum
    global chance
    incChance()
    logGuess(g, d)
    print(f"Guess incorrect, Please try again")
    x = input(f"Your last guess of {g} was {m} of the answer. Guess another number between {minNum} and {maxNum}: ")
    isInt(x)

def checkGuess(a, g):
    global chance
    global pastGuesses
    dist = guessDistance(a, g)
    if dist == 0:
        incChance()
        logGuess(g, dist)
        print(f" \n Congratulations, your guess of {g} was correct!")
        print(f"You got the answer in {chance} chances! Here is how this played out:  \n")
        t = PrettyTable(['Chance', 'Guess', 'Actual Distance'])
        for row in pastGuesses:
            t.add_row(row)
        print(t)

        sys.exit() #exits program
    elif dist > 50:
        incorrectGuess(g, dist, 'more than 50 away')
    elif dist <= 2:
        incorrectGuess(g, dist, 'within 2')
    elif dist <= 5:
        incorrectGuess(g, dist, 'within 5')
    elif dist <= 10:
        incorrectGuess(g, dist, 'within 10')
    elif dist <= 15:
        incorrectGuess(g, dist, 'within 15')
    elif dist <= 25:
        incorrectGuess(g, dist, 'within 25')
    elif dist <= 50:
        incorrectGuess(g, dist, 'within 50')



def guessInRange(guess):
    global minNum
    global maxNum
    global answer
    if(guess < minNum or guess > maxNum):
        guess = input(f"{guess} is not between {minNum} and {maxNum}. Please try again: ")
        isInt(guess)
    else:
        checkGuess(answer, guess)

def isInt(g):
    global minNum
    global maxNum
    try:
        int(g)
    except:
        guess = input(f"{g} is not a valid integer, please enter a valid integer between {minNum} and {maxNum}: ")
        isInt(guess)
    
    return guessInRange(int(g))


def main():
    global answer
    global minNum
    global maxNum
    guess = input(f"Type a number between {minNum} and {maxNum}: ")
    answer = randNum(minNum, maxNum) #The random number that is generated to guess against
    isInt(guess)

if __name__ == "__main__":
    main()
