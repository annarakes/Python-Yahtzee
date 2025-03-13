
import random
# Scorecard Helper Functions
#
# The Yahtzee scorecard is represented as a list of 13 elements
#     Each element in the list represents the score for
#     one of the spaces on the Yahtzee Scorecard
#       scorecard[0] -> Ones
#       scorecard[1] -> Twos
#       scorecard[2] -> Threes
#       scorecard[3] -> Fours
#       scorecard[4] -> Fives
#       scorecard[5] -> Sixes
#       scorecard[6] -> Three of a Kind
#       scorecard[7] -> Four of a Kind
#       scorecard[8] -> Full House
#       scorecard[9] -> Small Straight
#       scorecard[10] -> Large Straight
#       scorecard[11] -> Yahtzee
#       scorecard[12] -> Chance
#
# The functions below are helpful for working with the scorecard in Yahtzee

# The initializeScorecard function takes no inputs and returns an empty Scorecard
def initializeScorecard():
    scorecard = [None,None,None,None,None,None,None,None,None,None,None,None,None]
    return scorecard

# The printScorecard function takes a scorecard list as input
# and prints to the screen the Yahtzee Scorecard
def printScorecard(scorecard):
    choice = 0
    print("Scorecard:")
    print("-"*57)
    print(f'{"1. Ones:":<20} {str(scorecard[0]):<4}\t|\t{"7. Three of a Kind:":<20} {scorecard[6]}')
    print(f'{"2. Twos:":<20} {str(scorecard[1]):<4}\t|\t{"8. Four of a Kind:":<20} {scorecard[7]}')
    print(f'{"3. Threes:":<20} {str(scorecard[2]):<4}\t|\t{"9. Full House:":<20} {scorecard[8]}')
    print(f'{"4. Fours:":<20} {str(scorecard[3]):<4}\t|\t{"10. Small Straight:":<20} {scorecard[9]}')
    print(f'{"5. Fives:":<20} {str(scorecard[4]):<4}\t|\t{"11. Large Straight:":<20} {scorecard[10]}')
    print(f'{"6. Sixes:":<20} {str(scorecard[5]):<4}\t|\t{"12. Yahtzee:":<20} {scorecard[11]}')
    print(f'{"Upper Bonus:":<20} {str(calculateUpperBonus(scorecard)):<4}\t|\t{"13. Chance:":<20} {scorecard[12]}')
    print("-" * 57)
    print("Total Score:    ", calculateTotalScore(scorecard))
    print()

# The function calculateUpperBonus should take a scorecard as input
#   and return the upperBonus amount (as determined by Yahtzee rules)
#   Note: if the value for a given scoring category is None, it should be skipped
def calculateUpperBonus(scorecard):
    upper_total = 0
    for index in range(6):
        if (scorecard[index] != None):
            upper_total += scorecard[index]
    if (upper_total >= 63):
        upper_bonus  = 35
    else:
        upper_bonus = 0
    return upper_bonus

# The function calculateTotalScore should take a scorecard as input
#   and return the total score (as determined by Yahtzee rules)
#   Note: if the value for a given scoring category is None, it should be skipped
def calculateTotalScore(scorecard):
    total = 0
    upper_bonus = calculateUpperBonus(scorecard)
    for index in range(len(scorecard)):
        if scorecard[index] != None:
            total += scorecard[index]
    total += upper_bonus
    return total

# Dice Helper Functions
#   The functions below are helper functions for rolling dice

#The rollDie function simulates rolling one Die
#   It does not take any input and returns the results as
#   an integer from 1 to 6
def rollDie():
    return random.randint(1,6)

# The rollDiceSet function simulates rolling x number of Dice
#   It takes num_dice as an input
#   it returns a list with each element representing a single die
#   For example if it is called with num_dice = 3
#   It might return [4,2,5] representing
#       The first die rolled a 4
#       The second die rolled a 2
#       The third die rolled a 5
def rollDiceSet(num_dice):
    dice_list = []
    for current_dice in range(num_dice):
        dice_list.append(rollDie())
    return dice_list

# The printRoll function prints to the screen a simulation of rolling multiple dice
#   It takes a list as input and
#   outputs to the screen each element in the list with spaces between them
#   For example, if the input was [3,2,6]
#       It would output 3 2 6
def printRoll(dice_list):
    print(*dice_list)

# Selection Help Functions
#   These functions help in processing the user selections of
#   which die they want to keep and which die they want to re-roll

# The getSelections functions takes no input arguments
#   It returns a list variable where each element in the list
#   represents whether the user chose to keep or re-roll the corresponding
#   die in their turn. It assumes they are all separated by a space
#   For example,
#       If the user rolled 3 dice and got
#       6 6 2
#
#       Then the user typed on screen
#       K K R
#
#       It would return ['K','K','R']
#       Which represents keeping the two 6's but re-roll the 2
def getSelections():
    selection_input = input().upper().split(" ")
    return selection_input