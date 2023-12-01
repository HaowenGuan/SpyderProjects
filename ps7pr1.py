# 
# ps7pr1.py - Problem Set 7, Problem 1
#
# String-method puzzles
#

s1 = 'Three little kittens lost their mittens'
s2 = 'Star light, star bright'

# Example puzzle (puzzle 0):
# Count all occurrences of the letter T (both lower- and upper-case) in s1.
answer0 = s1.lower().count('t')     

# Put your solutions to the remaining string puzzles below.
answer1 = s1.replace('tt', 'pp')
answer2 = s2.split('r')
answer3 = s2.upper().replace('STAR', 'NIGHT')
answer4 = s1.lower().split('th')
answer5 = s2.replace('ight', 'ook').split(',')


#### Your solutions to the puzzles should be ABOVE this line. ####

# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 6):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))