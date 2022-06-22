import difficultySelection
import cardMechanics
import time



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

cards = cardMechanics.cardLine(cardMechanics.firstFour[0],cardMechanics.firstFour[1],cardMechanics.firstFour[2],
                               cardMechanics.firstFour[3])
'''
cards = arrangeCards.cardLine(arrangeCards.faceDown[0],arrangeCards.faceDown[1],arrangeCards.faceDown[2],
                      arrangeCards.faceDown[3])
print(cards)'''

# Guess whether first card is red or black
# Depending on result of guess, print whether the user has to give or take drinks
cardMechanics.isRedOrBlack()

'''
# Guess whether second card is higher or lower than first card
print(f"Your first card is worth {difficulty2} drinks")
print("Guess whether your card is higher or lower than your first card")
# Depending on result of guess, print whether the user has to give or take drinks
'''

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

