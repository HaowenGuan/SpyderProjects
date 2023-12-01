# 
# ps5pr10.py - Problem Set 5, Problem 10
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#%%
def add_odds(n):
    """
    Calculates the sum of the first 'n' odd numbers.
    It also prints each addition step.
    """
    result = 0
    for num in range(1, 2 * n + 1, 2):
        print(result, '+', num, '=', result + num)
        result += num
    return result
    

def test():
    """ performs test calls on the functions above """
    print(add_odds(5))
    print(add_odds(3))
    print(add_odds(7))
    print(add_odds(0))


#%%
def get_mult(n):
    """
    Prompts the user to enter a multiple of 'n' and keeps asking until a valid 
    multiple is entered.
    """
    value = int(input('Enter a multiple: '))
    while value % n > 0:
        value = int(input('Invalid input. Try again: '))
    return value