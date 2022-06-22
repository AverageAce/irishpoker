import cardFaces
import phaseOne
import random

def isRedOrBlack():
    red = [cardFaces.h2,cardFaces.h3,cardFaces.h4,cardFaces.h5,cardFaces.h6,cardFaces.h7,cardFaces.h8,cardFaces.h9,
           cardFaces.h10,cardFaces.hJ,cardFaces.hQ,cardFaces.hK,cardFaces.hA,cardFaces.d2,cardFaces.d3,cardFaces.d4,
           cardFaces.d5,cardFaces.d6,cardFaces.d7,cardFaces.d8,cardFaces.d9,cardFaces.d10,cardFaces.dJ,cardFaces.dQ,
           cardFaces.dK,cardFaces.dA]
    black = [cardFaces.s2,cardFaces.s3,cardFaces.s4,cardFaces.s5,cardFaces.s6,cardFaces.s7,cardFaces.s8,cardFaces.s9,
             cardFaces.s10,cardFaces.sJ,cardFaces.sQ,cardFaces.sK,cardFaces.sA,cardFaces.c2,cardFaces.c3,cardFaces.c4,
             cardFaces.c5,cardFaces.c6,cardFaces.c7,cardFaces.c8,cardFaces.c9,cardFaces.c10,cardFaces.cJ,cardFaces.cQ,
             cardFaces.cK,cardFaces.cA]
    guessChoices = ("red","black")
    guessRB = input()
    while guessRB not in guessChoices:
        print("Are you drunk already? Type 'Red' or 'Black'")
        guessRB = input()
        if guessRB in guessChoices:
            break
    if guessRB == 'red':
        if phaseOne.cardLine(phaseOne.firstFour[0]) in red:
            print("Nice job!")
            goodGuess = True
            return goodGuess
        else:
            print("You done fucked up.")
            goodGuess = False
            return goodGuess
    if guessRB == 'black':
        if phaseOne.cardLine(phaseOne.firstFour[0]) in black:
            print("Nice job!")
            goodGuess = True
            return goodGuess
        else:
            print("You done fucked up.")
            goodGuess = False
            return goodGuess
            # print(f"Give {difficultySelection.diffLevels[0]} drinks to another player")


