import cardFaces
import random


# Add cards to a list and shuffle the order
# Create list that contains all cards
cardDeck = [cardFaces.s2,cardFaces.s3,cardFaces.s4,cardFaces.s5,cardFaces.s6,cardFaces.s7,cardFaces.s8,cardFaces.s9,
            cardFaces.s10,cardFaces.sJ,cardFaces.sQ,cardFaces.sK,cardFaces.sA,cardFaces.h2,cardFaces.h3,cardFaces.h4,
            cardFaces.h5,cardFaces.h6,cardFaces.h7,cardFaces.h8,cardFaces.h9,cardFaces.h10,cardFaces.hJ,cardFaces.hQ,
            cardFaces.hK,cardFaces.hA,cardFaces.c2,cardFaces.c3,cardFaces.c4,cardFaces.c5,cardFaces.c6,cardFaces.c7,
            cardFaces.c8,cardFaces.c9,cardFaces.c10,cardFaces.cJ,cardFaces.cQ,cardFaces.cK,cardFaces.cA,cardFaces.d2,
            cardFaces.d3,cardFaces.d4,cardFaces.d5,cardFaces.d6,cardFaces.d7,cardFaces.d8,cardFaces.d9,cardFaces.d10,
            cardFaces.dJ,cardFaces.dQ,cardFaces.dK,cardFaces.dA]

# DEBUG: Print first 4 cards of unshuffled list
# print(cardDeck[0],cardDeck[1],cardDeck[2],cardDeck[3])

# Randomize order of list containing cards
random.shuffle(cardDeck)

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