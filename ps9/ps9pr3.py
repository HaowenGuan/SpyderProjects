#%%
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
    """ takes two parameters: a Player object p for the player whose move is being processed, 
        and a Board object b for the board on which the game is being played.
        This function should use the next_move method of the Player object to ask the player
        to select a column.
        Then it should use the add_checker method to add a checker to that column of the board.
        The function should return True if the move was successful, and False otherwise.
    """
    print(str(p) + "'s turn")
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    # print()
    if b.is_win_for(p.checker) == True:
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False
    
class RandomPlayer(Player):
    """ a subclass of Player that chooses at random from the available columns
    """
    def next_move(self, b):
        """ overrides the next_move method in Player class
        """
        available_cols = []
        for col in range(b.width):
            if b.can_add_to(col) == True:
                available_cols.append(col)
        self.num_moves += 1
        col = random.choice(available_cols)
        # while b.can_add_to(col) == False:
        #     col = random.randrange(b.width)
        return col
        
#%%
def test():
    # b1 = Board(2, 4)
    # b1.add_checkers('001122')
    # process_move(Player('X'), b1)
    # process_move(Player('O'), b1)
    # b1.remove_checker(3)
    # b1.remove_checker(3)
    # process_move(Player('O'), b1)
    # process_move(Player('X'), b1)

    connect_four(RandomPlayer('X'), RandomPlayer('O'))

