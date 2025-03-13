##############################################
#                                            #
#              Anna Rakes                    #
#           Yahtzee project                  #
#                                            #
##############################################

import random
import yahtzeeHelper

# The function makeScoreChoice should take
#   a scorecard list as an input parameter and
#   return the number for the scoring category selected by the user
#   If the scoring category has already been used
#       It should tell the user that category has already been used
#       and make the user keep selecting
#       A category has already been used if it has a score even if it is 0

################## Logic Comments
# 1. Ask the user what category they want to select by inputting a number for the corresponding category
# 2. Find the index in the list of the category they selected. If they inputted 7, for category 7 (three of a kind),
#    the index in scorecard is 6.
# 3. Compare value of scorecard at the index specified above to 'None'.
# 4. Use a while loop if their selection equals something other than None to keep asking the user to pick a category
#    until their selection is in a category that has the string 'None'.
# 5. Each iteration of the loop will print "the category has already been selected" and to "keep selecting"
# 6. Once they pick a category that has a value of 'None' in its corresponding index in the list, it will exit the loop
#    and print their input.
def makeScoreChoice(scorecard):
    score_choice = int(input("Select a scoring category:"))
    while scorecard[score_choice - 1] != None:
        print("This category has already been used")
        score_choice = int(input("Select a different scoring category:"))
    final_choice = score_choice
    return final_choice


#The function countByNumber should take
#   roll_list which is a list representing each roll as input
#   and
#   return a List that contains 6 elements representing
#       the count of die for each possible number
#
#   For example:
#       if roll_list = [2,5,3,2,2]
#       It should return a list of [0,3,1,0,1,0]
#           This represents:
#               0 die showing 1
#               3 dice showing 2
#               1 die showing 3
#               0 die showing 4
#               1 die showing 5
#               0 die showing 6
################## Logic Comments
# 1. Define function countByNumber, whose input parameter is roll_list. The list inputted will have 5 digits
#    corresponding to each die roll.
# 2. Initialize a count of 0 for each of the numbers on the die (1-6_
# 3. Create a for loop to iterate through each number rolled in the roll list.
# 4. Create if else statements to assign the number of the roll with one of the 6 number counts. Once inside the if
#    statement, add one to its corresponding number in the initialized count.
# 5. For example, if the roll was a 3, it would cycle through to the elif statement for 3 and change the count in its
#    corresponding number count from a 0 to a 1.
# 6. Add the count for each number to a list and return it.
def countByNumber(roll_list):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    for roll in roll_list:
        if roll == 1:
            count_1 += 1
        elif roll == 2:
            count_2 += 1
        elif roll == 3:
            count_3 += 1
        elif roll == 4:
            count_4 += 1
        elif roll == 5:
            count_5 += 1
        elif roll == 6:
            count_6 += 1
    die_count = [count_1, count_2, count_3, count_4, count_5, count_6]
    return die_count


# The function sumRoll takes one input parameter
#   The roll_list which is a list of the results of rolling your dice
#   It returns the sum of all of the die in the roll

############### Logic Comments
# 1. To find the sum of all of the die in the roll (list roll_list) I will use the sum() function.
# 2. Inside the sum function I will insert the parameter, roll_list.
# 3. I will assign the sum of roll_list to the object sum_of_roll and return it.
def sumRoll(roll_list):
    sum_of_roll = sum(roll_list)
    return sum_of_roll



# The function calculateNumChoice takes two input parameters:
#   The number you want to calculate
#   The roll_list which is a list of the results of rolling your dice
# It should return:
#   The calculated score for the selected category
# This function should be used for the categories - Ones,Twos,Threes,Fours,Fives,Sixes
# The logic for calculating the score should follow the Yahtzee rules
# An Example would be
#   if your roll_list looked like [3,1,2,1,1]
#   and you wanted to calculate 1's
#   you would call the function like calculateNumChoice(1,roll_list)
#   The return value should equal 3

############### Logic Comments
# 1. I first would want to calculate how many times my selected number showed up in my roll list.
# 2. I can do this with the count() function. For example, if number represents the number I want to calculate and
#    roll_list represents my list, I would do roll_list.count(number) and assign it to variable frequency
# 3. Once I calculated the occurrences of the number (frequency), I would create an object called score which would
#    calculate the number of occurrences times the number itself. For example: score = frequency*number
#    I would then return object score.
def calculateNumChoice(number,roll_list):
    frequency = roll_list.count(number)
    score = frequency*number
    return score


# The function calculateOfKind takes two input parameters:
#       how_many - Represents how many of a given kind you are looking for (3 for three of a kind, 4 for 4 of a kind)
#       roll_list - A list of the dice that were rolled
#   It should return the calculated score per Yahtzee rules
#   For example:
#       With input parameters values of:
#           how_many = 3
#           roll_list = [5,4,3,4,4]
#       It would return:
#           20
################### Logic Comments
# 1. To first figure out if my roll has multiples of numbers, I will use the countByNumber function I created and then
#    the input parameter will be the roll list. I will store this into a variable called roll_counts
# 2. I will then use a for loop to go through each number in roll_counts (1 through 6)
# 3. For each number, I want to find out if it is greater than or equal to how many of a kind I want. For example, if
#    4 was the input parameter for how_many and roll_counts had a value of 4 in the 1 position (0 index), it would
#    enter the if statement.
# 4. Within the if statement, if the number in roll_counts meets how_many, there will be another one that checks to
#    see if the player wanted to go for yahtzee, meaning how_many would be 5 and score would be set equal to 50.
# 5. If they don't want to go for yahtzee, an else statement is used and I'll calculate the sum of all the die by
#    calling the sumRoll function for the actual roll_list.
#    If there is no number that shows up as many times as how_many, score will equal 0.
def calculateOfKind(how_many,roll_list):
    roll_counts = countByNumber(roll_list)
    for number in roll_counts:
        if number>=how_many:
            if how_many == 5:
                score = 50
            else:
                score = sumRoll(roll_list)
            break
        else:
            score = 0
    return score


#The function calculateFullHouse should have an input parameter
#       roll_list - a list representing the rolled dice
#   It should return 25 if the roll meets the rules of a full house
#       or 0 if it does not
############################## Logic Comments
# 1. I will again call the countByNumber function and input roll_list to see how many of each number the roll produces.
# 2. This will be stored in an object called roll_counts
# 3. For this function, I want to check that there are 2 of a number and 3 of a different number, so I will initialize
#    two boolean objects starting at false. At the end, if they meet the criteria, both should be true and the score
#    will be 25.
# 3. I will again use a for statement to iterate through each number in roll_counts. To check my two conditions, I will
#    create if else statements that checks to see if the number in roll_counts is equal to 2 or 3. If it meets the
#    criteria, the corresponding test will be made to true.
# 4. Once it has iterated through each of the counts of the numbers, I will check to see if test 2 equals true and test
#    3 also equals two. If they both do, the score will be 25. If not, the score will be 0.
def calculateFullHouse(roll_list):
    roll_counts = countByNumber(roll_list)
    test_2 = False
    test_3 = False
    for number in roll_counts:
        if number == 2:
            test_2 = True
        elif number == 3:
            test_3 = True
    if (test_2 == True) and (test_3 == True):
        score = 25
    else:
        score = 0
    return score


#The function calculateStraight should have three input parameters:
#       num_straight - a number representing how many numbers in a row the straight requires
#       roll_list - a list representing the rolled dice
#       success_score - The score that should be returned if it meets the criteria successfully
#   It should return the appropriate score base on Yahtzee rules for a straight
######################################### Logic Comments
# 1. Once again I will call the function countByNumber, inputting roll_list and assigning it to roll_counts. I am using
#    this function because it will put my rolls in ascending order. Ideally, a straight put into countByNumber will
#    produce a list that has 5 consecutive ones.
# 2. I will initialize a variable called consecutive and set it to 0.
# 3. I will iterate through each number in roll_counts with a for statement. If the number is greater than 0, meaning it
#    shows up atleast once in the roll_list. It will add one to the consecutive variable.
# 4. However, if the number is 0, that means it never showed up in the list and is no longer consecutive, so I will set
#    consecutive back to 0
# 5. If the roll_counts has 5 consecutive numbers, once it hits the 5th number, it will set consecutive to 5 and check
#    to see if it is equal to num_straight (the number representing how many numbers in a row it should be).
# 6. If they are equal to each other, it will exit the for statement and assign the success_score to score. If not,
#    the score will be 0.
def calculateStraight(num_straight,roll_list,success_score):
    roll_counts = countByNumber(roll_list)
    consecutive = 0
    for number in roll_counts:
        if number > 0:
            consecutive += 1
            if consecutive == num_straight:
                break
        else:
            consecutive = 0
    if consecutive >= num_straight:
        score = success_score
    else:
        score = 0
    return score

#The function calculateChance should have an input parameter
#       roll_list - a list representing the rolled dice
#   It should return the score for chance based on Yahtzee rules
################################# Logic Comments
# 1. Since chance is calculated by summing up the roll on each dice, I will call the sumRoll function
# 2. I will then input the roll_list and store it into an object, score.
# 3. I will then return score.
def calculateChance(roll_list):
    score = sumRoll(roll_list)
    return score

# The function calculateCategoryScore takes three input parameters:
#       scorecard - a list representing the current scorecard
#       choice - a number representing the selected scoring category
#       roll_list - a list representing the current roll of dice
#   It should return
#       An updated scorecard list with the score for the selected category filled out
############################## Logic Comments
# 1. Choices less than 6 were calculated from function calculateNumChoice, to find the product of the number selected,
#    which will be inputted into the parameter choice, times how many times it showed up.
# 2. Choice 7 is for 3 of a kind, so I will call the function calculateOfKind and specify 3 for how many.
# 3. Choice 8 is for 4 of a kind, so I will call the function calculateofKind and specify 4 for how many.
# 4. Choice 9 is for a full house, so I will call the function calculateFullHouse and only input roll_list, the only
#    parameter needed.
# 5. Choice 10 is for a small straight, so I will call calculateStraight, specifying the number of straight I want is
#    4 and that produces a score of 30 if met.
# 6. Choice 11 is for a large straight, so I will call calculateStraight, specifying the number of straight I want is
#    5 and that produces a score of 40 if met.
# 7. Choice 12 is for a yahtzee, which is technically 5 of a kind, so I will call the function calculateOfKind, but
#    how_many will be set to 5.
# 8. The last score is chance, which will call the function calculateChance.

def calculateCategoryScore(scorecard,choice,roll_list):
    score = 0
    if choice <= 6:
        score = calculateNumChoice(choice, roll_list)
    elif choice == 7:
        score = calculateOfKind(3, roll_list)
    elif choice == 8:
        score = calculateOfKind(4, roll_list)
    elif choice == 9:
        score = calculateFullHouse(roll_list)
    elif choice == 10:
        score = calculateStraight(4, roll_list, 30)
    elif choice == 11:
        score = calculateStraight(5, roll_list, 40)
    elif choice == 12:
        score = calculateOfKind(5, roll_list)
    else:
        score = calculateChance(roll_list)
    scorecard[choice - 1] = score
    return scorecard


# The function takeTurn simulates one turn for a player
# It has one input parameter, the current scorecard for the player
# It returns the updated scorecard after their turn
# A given turn (based on Yahtzee rules) consists of
#       1. An initial roll of 5 Die
#       2. The user may decide to keep or re-roll any number of the die
#       3. The user re-rolls any die they want or stop rolling if they want to keep all 5 die
#       4. The user can repeat this process so they can re-roll a second time if they choice
#       5. After deciding to keep all die or rolling a total of 3 times,
#       6. The user must choose a scoring category for their turn
#       7. After choosing a scoring category, the category score should be updated for the dice roll
#       8. The user's scorecard should be updated and returned
def takeTurn(scorecard):
    roll_result = yahtzeeHelper.rollDiceSet(5)
    rolls = 0
    num_keep = 0
    while (rolls < 2 and num_keep < 5):
        num_keep = 0
        yahtzeeHelper.printRoll(roll_result)
        selection_list = yahtzeeHelper.getSelections()
        for index in range(5):
            if selection_list[index] == 'R':
                roll_result[index] = yahtzeeHelper.rollDie()
            else:
                num_keep += 1
        rolls += 1

    print("Your final roll is")
    yahtzeeHelper.printRoll(roll_result)
    yahtzeeHelper.printScorecard(scorecard)
    choice = makeScoreChoice(scorecard)
    scorecard = calculateCategoryScore(scorecard, choice, roll_result)
    return scorecard

#The function playGame simulates playing Yahtzee for a single player game
#   It has not input parameters and no return value
#   A Yahtzee game consists of
#       1. Initializing a scorecard
#       2. Having the user keep taking turns until their scorecard is full
#       3. The user should see their scorecard after each turn
#       4. Once the game is complete the user should see their final scorecard
def playGame():
    scorecard = yahtzeeHelper.initializeScorecard()
    turns = 0
    while (turns < 13):
        scorecard = takeTurn(scorecard)
        turns += 1
        yahtzeeHelper.printScorecard(scorecard)
        if turns < 13:
            print("Starting Next Turn")

if __name__ == '__main__':
    playGame()
