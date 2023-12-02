#%%
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    """ a data type for a Connect Four player with a name and checker
    """
    def __init__(self, checker):
        """ initialize Player
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ Returns a string that represents a Player object
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing the checker's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, b):
        """ accepts a Board object as a parameter and returns the column where the player wants to make the next move.
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            print('Invalid column, try again!')

#%%
def test():
    p1 = Player('X')
    b = Board(6, 7)
    print(p1)
    print(p1.opponent_checker())
    print(p1.next_move(b))
    print(p1.num_moves)
