import cardFaces
import shuffleDeck

# Create a set of four face down cards
faceDown = (cardFaces.backFace,cardFaces.backFace,cardFaces.backFace,cardFaces.backFace)

# Get first four cards from shuffled deck
firstFour = (shuffleDeck.cardDeck[0],shuffleDeck.cardDeck[1],shuffleDeck.cardDeck[2],shuffleDeck.cardDeck[3])

# print first four cards in-line
def cardLine(card1,card2,card3,card4):
    l1 = card1.split('\n')
    l2 = card2.split('\n')
    l3 = card3.split('\n')
    l4 = card4.split('\n')
    for i in range(min(len(l1),len(l2),len(l3),len(l4))):
        print(l1[i]+'\t'+l2[i]+'\t'+l3[i]+'\t'+l4[i])

# cardLine(firstFour[0],firstFour[1],firstFour[2],firstFour[3])

# cardLine(faceDown[0],faceDown[1],faceDown[2],faceDown[3])

# print(firstFour[0],firstFour[1],firstFour[2],firstFour[3])