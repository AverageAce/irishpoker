import difficultySelection
import cardMechanics
import time



card1 = cardMechanics.cardDeck[0]
card2 = cardMechanics.cardDeck[1]
card3 = cardMechanics.cardDeck[2]
card4 = cardMechanics.cardDeck[3]

# Opening sequence: rules and presentation of cards

print("---Phase 1---")
# Show 4 face down cards with labels above each column corresponding to the 'difficulty' values
print("You have been dealt 4 cards, face down")
time.sleep(1)
print(" ")
print("You will attempt to guess each card from left to right")
time.sleep(1)
print(" ")
print("Each card you guess successfully will be worth a certain number of drinks for whomever you prefer")
time.sleep(1)
print(" ")
print("Each card you guess incorrectly will be worth the same amount of drinks for yourself")
time.sleep(1)
print(" ")
print(f"Your first card is worth {difficultySelection.diffLevels[0]} drinks")
time.sleep(1)
print(" ")
print("Guess whether your first card is red or black")
time.sleep(1)
print(' ')


print(f'   {difficultySelection.diffLevels[0]}       {difficultySelection.diffLevels[1]}       '
      f'{difficultySelection.diffLevels[2]}       {difficultySelection.diffLevels[3]}   ')

print(f'   {card1.cardBack}     {card2.cardBack}     {card3.cardBack}     {card4.cardBack}   ')
# print(f'   {card1.faceValue}       {card2.faceValue}       {card3.faceValue}       {card4.faceValue}   ')

'''
cards = arrangeCards.cardLine(arrangeCards.faceDown[0],arrangeCards.faceDown[1],arrangeCards.faceDown[2],
                      arrangeCards.faceDown[3])
print(cards)'''
guessChoices = ("red","black")
guessRB = input()
if guessRB not in guessChoices:
      print("Are you drunk already? Type 'Red' or 'Black'")
      guessRB = input()

elif guessRB in guessChoices:
      print(f'DEBUG: User input: {guessRB}')

if guessRB == 'red':
      if card1.suite == 'hearts':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("Nice job!")
            print(f'The card was {card1.faceLabel} of {card1.suite}')

      elif card1.suite == 'diamonds':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("Nice job!")
            print(f'The card was {card1.faceLabel} of {card1.suite}')

      elif card1.suite == 'spades':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("You done fucked up.")
            print(f'The card was {card1.faceLabel} of {card1.suite}')

      elif card1.suite == 'clubs':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("You done fucked up!")
            print(f'The card was {card1.faceLabel} of {card1.suite}')


if guessRB == 'black':
      if card1.suite == 'spades':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("Nice job!")
            print(f'The card was {card1.faceLabel} of {card1.suite}')

      elif card1.suite == 'clubs':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("Nice job!")
            print(f'The card was {card1.faceLabel} of {card1.suite}')

      elif card1.suite == 'hearts':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("You done fucked up.")
            print(f'The card was {card1.faceLabel} of {card1.suite}')

      elif card1.suite == 'diamonds':
            print(f'DEBUG: Choice selected: {guessRB}')
            print("You done fucked up.")
            print(f'The card was {card1.faceLabel} of {card1.suite}')


# Guess whether first card is red or black
# Depending on result of guess, print whether the user has to give or take drinks
# cardMechanics.isRedOrBlack()

print(f'   {difficultySelection.diffLevels[0]}       {difficultySelection.diffLevels[1]}       '
      f'{difficultySelection.diffLevels[2]}       {difficultySelection.diffLevels[3]}   ')

print(f'   {card1.faceLabel}     {card2.cardBack}     {card3.cardBack}     {card4.cardBack}   ')
time.sleep(1)
print(" ")
# print(f'   {card1.faceValue}       {card2.faceValue}       {card3.faceValue}       {card4.faceValue}   ')

# guessRedBlack = cardMechanics.isRedOrBlack().guessRB


# # DEBUG
# card1 = cardMechanics.cardDeck[0]
# card2 = cardMechanics.cardDeck[0]
# card3 = cardMechanics.cardDeck[1]
# card4 = cardMechanics.cardDeck[2]
#
# print(f'   {difficultySelection.diffLevels[0]}       {difficultySelection.diffLevels[1]}       '
#       f'{difficultySelection.diffLevels[2]}       {difficultySelection.diffLevels[3]}   ')
#
# print(f'   {card1.faceLabel}     {card2.faceLabel}     {card3.faceLabel}     {card4.faceLabel}   ')
#
# # Guess whether second card is higher or lower than first card
print(f"Your second card is worth {difficultySelection.diffLevels[1]} drinks")
time.sleep(1)
print(" ")
print("Guess whether your second card is higher or lower than your first card")
time.sleep(1)
print(" ")

guessChoices = ('higher','lower')
guessHL = input()

if guessHL not in guessChoices:
      print("Are you drunk already? Type 'Red' or 'Black'")
      guessRB = input()

elif guessHL in guessChoices:
      print(f'DEBUG: User input: {guessHL}')

if guessHL == 'higher':
      if card2.faceValue == card1.faceValue:
            for x in cardMechanics.cardDeck:
                  if x == cardMechanics.cardDeck[0]:
                        continue
                  elif x == cardMechanics.cardDeck[1]:
                        continue
                  elif x == cardMechanics.cardDeck[2]:
                        continue
                  elif x == cardMechanics.cardDeck[3]:
                        continue
                  elif x == card2.faceValue:
                        continue
                  elif x != card2.faceValue:
                        card2 = x
                        break
      if card2.faceValue > card1.faceValue:
            print('Nice job!')
      elif card2.faceValue < card1.faceValue:
            print('You done fucked up, drink!')

if guessHL == 'lower':
      if card2.faceValue == card1.faceValue:
            for x in cardMechanics.cardDeck:
                  if x == cardMechanics.cardDeck[0]:
                        continue
                  elif x == cardMechanics.cardDeck[1]:
                        continue
                  elif x == cardMechanics.cardDeck[2]:
                        continue
                  elif x == cardMechanics.cardDeck[3]:
                        continue
                  elif x == card2.faceValue:
                        continue
                  elif x != card2.faceValue:
                        card2 = x
                        break
      if card2.faceValue < card1.faceValue:
            print('Nice job!')
      elif card2.faceValue > card1.faceValue:
            print('You done fucked up, drink!')

print(f'   {difficultySelection.diffLevels[0]}       {difficultySelection.diffLevels[1]}       '
      f'{difficultySelection.diffLevels[2]}       {difficultySelection.diffLevels[3]}   ')

print(f'   {card1.faceLabel}     {card2.faceLabel}     {card3.cardBack}     {card4.cardBack}   ')

# Depending on result of guess, print whether the user has to give or take drinks


'''
# Guess whether third card is in between or outside first two cards
print(f"Your first card is worth {difficulty3} drinks")
print("Guess whether your third card is in between or outside your first two cards")
# Depending on result of guess, print whether the user has to give or take drinks
'''

'''
# Guess the suite of the fourth card
print(f"Your first card is worth {difficulty4} drinks")
print("Guess the suite of your final card")
# Depending on result of guess, print whether the user has to give or take drinks
'''

# Keep cards and continue to PHASE 2

