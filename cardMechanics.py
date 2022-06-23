import cardFaces
import random

# Shuffle Deck
# Add cards to a list and shuffle the order
# Create list that contains all cards
cardDeck = [cardFaces.S2(),cardFaces.S3(),cardFaces.S4(),cardFaces.S5(),cardFaces.S6(),cardFaces.S7(),cardFaces.S8(),
            cardFaces.S9(),cardFaces.S10(),cardFaces.SJ(),cardFaces.SQ(),cardFaces.SK(),cardFaces.SA(),cardFaces.H2(),
            cardFaces.H3(),cardFaces.H4(),cardFaces.H5(),cardFaces.H6(),cardFaces.H7(),cardFaces.H8(),cardFaces.H9(),
            cardFaces.H10(),cardFaces.HJ(),cardFaces.HQ(),cardFaces.HK(),cardFaces.HA(),cardFaces.C2(),cardFaces.C3(),
            cardFaces.C4(),cardFaces.C5(),cardFaces.C6(),cardFaces.C7(),cardFaces.C8(),cardFaces.C9(),cardFaces.C10(),
            cardFaces.CJ(),cardFaces.CQ(),cardFaces.CK(),cardFaces.CA(),cardFaces.D2(),cardFaces.D3(),cardFaces.D4(),
            cardFaces.D5(),cardFaces.D6(),cardFaces.D7(),cardFaces.D8(),cardFaces.D9(),cardFaces.D10(),cardFaces.DJ(),
            cardFaces.DQ(),cardFaces.DK(),cardFaces.DA()]

red = [cardFaces.H2(), cardFaces.H3(), cardFaces.H4(), cardFaces.H5(), cardFaces.H6(), cardFaces.H7(), cardFaces.H8(),
       cardFaces.H9(), cardFaces.H10(), cardFaces.HJ(), cardFaces.HQ(), cardFaces.HK(), cardFaces.HA(), cardFaces.D2(),
       cardFaces.D3(), cardFaces.D4(), cardFaces.D5(), cardFaces.D6(), cardFaces.D7(), cardFaces.D8(), cardFaces.D9(),
       cardFaces.D10(), cardFaces.DJ(), cardFaces.DQ(), cardFaces.DK(), cardFaces.DA()]
black = [cardFaces.S2(), cardFaces.S3(), cardFaces.S4(), cardFaces.S5(), cardFaces.S6(), cardFaces.S7(), cardFaces.S8(),
         cardFaces.S9(), cardFaces.S10(), cardFaces.SJ(), cardFaces.SQ(), cardFaces.SK(), cardFaces.SA(),
         cardFaces.C2(),cardFaces.C3(), cardFaces.C4(), cardFaces.C5(), cardFaces.C6(), cardFaces.C7(), cardFaces.C8(),
         cardFaces.C9(),cardFaces.C10(), cardFaces.CJ(), cardFaces.CQ(), cardFaces.CK(), cardFaces.CA()]

# # DEBUG: Print first 4 cards of unshuffled list
# # print(cardDeck[0],cardDeck[1],cardDeck[2],cardDeck[3])
# card1 = cardDeck[0]
# card2 = cardDeck[1]
#
# print(f"{card1.faceValue} of {card1.suite}")
# print(f"{card2.faceValue} of {card2.suite}")
#
# Randomize order of list containing cards
random.shuffle(cardDeck)

firstFour = cardDeck[0],cardDeck[1],cardDeck[2],cardDeck[3]
# # DEBUG: Print first four cards again to verify shuffle
# card1 = cardDeck[0]
# card2 = cardDeck[1]
#
# print(f"{card1.faceValue} of {card1.suite}")
# print(f"{card2.faceValue} of {card2.suite}")

# DEBUG: Print first four cards again to verify shuffle
# print(cardDeck[0],cardDeck[1],cardDeck[2],cardDeck[3])

# DEBUG: Print shuffled deck
'''
print(cardDeck[0],cardDeck[1],cardDeck[2],cardDeck[3],cardDeck[4],cardDeck[5],cardDeck[6],cardDeck[7],cardDeck[8],
      cardDeck[9],cardDeck[10],cardDeck[11],cardDeck[12],cardDeck[13],cardDeck[14],cardDeck[15],cardDeck[16],
      cardDeck[17],cardDeck[18],cardDeck[19],cardDeck[20],cardDeck[21],cardDeck[22],cardDeck[23],cardDeck[24],
      cardDeck[25],cardDeck[26],cardDeck[27],cardDeck[28],cardDeck[29],cardDeck[30],cardDeck[31],cardDeck[32],
      cardDeck[33],cardDeck[34],cardDeck[35],cardDeck[36],cardDeck[37],cardDeck[38],cardDeck[39],cardDeck[40],
      cardDeck[41],cardDeck[42],cardDeck[43],cardDeck[44],cardDeck[45],cardDeck[46],cardDeck[47],cardDeck[48],
      cardDeck[49],cardDeck[50],cardDeck[51])'''

# # ArrangeCards
# # Create a set of four face down cards
# faceDown = (cardFaces.backFace,cardFaces.backFace,cardFaces.backFace,cardFaces.backFace)
#
# # Get first four cards from shuffled deck
# firstFour = (cardDeck[0],cardDeck[1],cardDeck[2],cardDeck[3])
#
# # Splitting function: print first four cards in-line
# # FIGURE OUT HOW THIS WORKS AND COMMENT IT
# '''
# def cardLine(card1,card2,card3,card4):
#     l1 = card1.split('\n')
#     l2 = card2.split('\n')
#     l3 = card3.split('\n')
#     l4 = card4.split('\n')
#     for i in range(min(len(l1),len(l2),len(l3),len(l4))):
#         print(l1[i]+'\t'+l2[i]+'\t'+l3[i]+'\t'+l4[i])
#         '''
#
# Red or Black
def isRedOrBlack():
    guessChoices = ("red","black")
    guessRB = input()
    if guessRB not in guessChoices:
        print("Are you drunk already? Type 'Red' or 'Black'")
        guessRB = input()
        return guessRB
    elif guessRB in guessChoices:
        print(f'DEBUG: User input: {guessRB}')
        return guessRB

    # if guessRB == 'red':
    #     if cardDeck[0] in red:
    #         print(f'DEBUG: Choice selected: {guessRB}')
    #         print("Nice job!")
    #         goodGuess = True
    #         return goodGuess
    #     elif cardDeck[0] in black:
    #         print(f'DEBUG: Choice selected: {guessRB}')
    #         print("You done fucked up.")
    #         goodGuess = False
    #         return goodGuess
    #
    # if guessRB == 'black':
    #     if cardDeck[0] in black:
    #         print(f'DEBUG: Choice selected: {guessRB}')
    #         print("Nice job!")
    #         goodGuess = True
    #         return goodGuess
    #     elif cardDeck[0] in red:
    #         print(f'DEBUG: Choice selected: {guessRB}')
    #         print("You done fucked up.")
    #         goodGuess = False
    #         return goodGuess
            # print(f"Give {difficultySelection.diffLevels[0]} drinks to another player")

