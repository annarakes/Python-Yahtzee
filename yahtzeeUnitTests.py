##############################################
#                                            #
#              Anna Rakes                    #
#           Yahtzee project                  #
#                                            #
##############################################

import yahtzeeHelper
import yahtzee

#Using the functions in yahtzee-helper
#write the function calls to

#1. Initialize a scorecard list
print("Running Test 1")
scorecard = yahtzeeHelper.initializeScorecard()

#2. Print Empty Scorecard
print("Running Test 2")
yahtzeeHelper.printScorecard(scorecard)

#3 Print a sample scorecard for the worst possible score.
#   In other words, the user has 0 points for every scoring category
#   For example, bad_scorecard = [0,0,0,0,0,0,0,0,0,0,0,0,0]
print("Running Test 3")
bad_scorecard = [0,0,0,0,0,0,0,0,0,0,0,0,0]
yahtzeeHelper.printScorecard(bad_scorecard)


#4 Print a sample scorecard for the best possible score.
#   In other words, the user got maximum points for every category
#   For example, great_scorecard = [5,10,15,20,25,30,30,30,25,30,40,50,30]
print("Running Test 4")
great_scorecard = [5,10,15,20,25,30,30,30,25,30,40,50,30]
yahtzeeHelper.printScorecard(great_scorecard)

#5. Write the code to roll a die and print out the result
#       In the form User rolled a X
#       So if the roll was a 5
#       Output would be User rolled a 5
print("Running Test 5")
print(yahtzeeHelper.rollDie())

#6. Write the code to simulate rolling 3 dice and print the output
#       For example if the user rolled a 6, a 2 , and a 1
#       The output would be:
#       6 2 1
print("Running Test 6")
print(yahtzeeHelper.rollDiceSet(3))

#7. Write the code to simulate rolling 4 dice and output the result
print("Running Test 7")
print(yahtzeeHelper.rollDiceSet(4))

#8. Create your own scorecard list, make sure it meets the criteria
#       to earn the upper bonus.
#       Write the code to print out the scorecard list your created and make sure
#       the output is correct
print("Running Test 8")
my_scorecard = [5,6,9,12,15,18,14,16,25,30,40,0,20]
yahtzeeHelper.printScorecard(my_scorecard)

############################################################################
############################################################################
############################################################################
########ALL TESTS BELOW THIS POINT REQUIRE YOU TO FIRST IMPLEMENT YOUR LOGIC IN yahtzee.py
############################################################################
############################################################################
############################################################################

#9. In order to build this test, you need to implement the logic for
#       makeScoreChoice in yahtzee.py
#    Write the code using the scorecard:
#       scorecard = [None,None,9,12,16,None,0,None,25,30,None,None,17]
#    to ask the user for their selection and output their selection
#    Try with the following choices:
#       1 -> Should be successful
#       3 -> Should tell the user it is in use and make them pick again
#       8 -> Should be successful
print("Running Test 9")
scorecard = [None, None, 9, 12, 16, None, 0, None, 25, 30, None, None, 17]
print(yahtzee.makeScoreChoice(scorecard))

#10. In order to build this test, you need to implement the logic for
#       countByNumber in yahtzee.py
#    Write the code using the dice roll of
#       dice_roll = [4,6,6,1,3]
#   to output the number of dice per each number
#   Your output should be [1,0,1,1,0,2]
print("Running Test 10")
dice_roll = [4,6,6,1,3]
print(yahtzee.countByNumber(dice_roll))

#11, In order to build this test, you meed to implement the logic for
#       sumRoll in yahtzee.py
#   Write the code using the dice roll of
#       dice_roll = [2,5,3,5,6]
#   to output the sum of all dice
#   Your output should be 21
print("Running Test 11")
dice_roll = [2,5,3,5,6]
print(yahtzee.sumRoll(dice_roll))

#12, In order to build this test, you meed to implement the logic for
#       calculateOfKind in yahtzee.py
#   Write the calls for the following executions
print("Running Test 12")
#       Run 1:
#           how_many = 3
#           dice_roll = [2,6,5,6,6]
#           The output should be 25
print(yahtzee.calculateOfKind(3, [2,6,5,6,6]))
#       Run 2:
#           how_many = 4
#           dice_roll = [2,6,5,6,6]
#           The output should be 0
print(yahtzee.calculateOfKind(4, [2,6,5,6,6]))
#       Run 3:
#           how_many = 4
#           dice_roll = [6,6,5,6,6]
#           The output should be 29
print(yahtzee.calculateOfKind(4, [6,6,5,6,6]))
print(yahtzee.calculateOfKind(5, [5,5,5,5,5]))

#13, In order to build this test, you meed to implement the logic for
#       calculateFullHouse in yahtzee.py
#    Write the calls for the following executions:
print("Running Test 13")
#       Run 1:
#            dice_roll = [5,2,5,2,5]
#            The output should be 25
print(yahtzee.calculateFullHouse([5,2,5,2,5]))
#       Run 2:
#            dice_roll = [5,2,5,2,3]
#            The output should be 0
print(yahtzee.calculateFullHouse([5,2,5,2,3]))


#14, In order to build this test, you meed to implement the logic for
#       calculateStraight in yahtzee.py
#    Write 3 calls to the calculateStraight function
print("Running Test 14")
#       Call 1 -> This call should be trying to score a small straight and be successful
print(yahtzee.calculateStraight(4, [2,2,3,4,5], 30))
#       Call 2 -> This call should be trying to score a large straight and be successful
print(yahtzee.calculateStraight(5, [5,3,2,4,1,], 40))
#       Call 3 -> This call should be trying to score a large straight and be unsuccessful
print(yahtzee.calculateStraight(5, [2,2,6,1,3], 40))


#15, In order to build this test, you need to implement the logic for
#       calculateChance in yahtzee.py
#    Write a sample call to calculateChance function
#       You should make up your own input and ensure the output is correct as you expect it
print("Running Test 15")
print(yahtzee.calculateChance([5,1,3,2,3]))
print(yahtzee.calculateChance([6,3,3,2,4]))


#16, In order to build this test, you need to implement the logic for
#       calculateCategoryScore in yahtzee.py
#   Write 3 sample calls to calculateCategoryScore function
print("Running Test 16")
#       Call 1 -> This call should be the user selecting a number category (Ones through Sixes)
#                   and return the appropriate score
scorecard = yahtzeeHelper.initializeScorecard()
yahtzeeHelper.printScorecard(scorecard)
roll_list = [3,5,2,2,1]
print(yahtzee.calculateCategoryScore(scorecard, 2, roll_list))

#       Call 2 -> This call should be the user selecting four of a kind
#                   and return the appropriate score
roll_list = [3,3,3,5,3]
print(yahtzee.calculateCategoryScore(scorecard, 8, roll_list))

#       Call 3 -> This call should be the user selecting Large Straight
#                   and return the appropriate score
roll_list = [5,3,4,2,1]
print(yahtzee.calculateCategoryScore(scorecard, 11, roll_list))

