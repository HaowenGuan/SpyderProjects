#%%
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ special constructor for AIPlayer
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ Returns a string that represents an AIPlayer object
        """
        return super().__repr__() + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, 
            and that returns the index of the column with the maximum score.
        """
        max_score = max(scores)
        max_score_cols = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_score_cols += [i]
        if self.tiebreak == 'LEFT':
            return max_score_cols[0]
        elif self.tiebreak == 'RIGHT':
            return max_score_cols[-1]
        else:
            return random.choice(max_score_cols)
        
    def scores_for(self, b):
        """
        """
        ans = []
        for col in range(b.width):
            if b.can_add_to(col) == False:
                ans.append(-1)
            elif b.is_win_for(self.checker) == True:
                ans.append(100)
            elif b.is_win_for(self.opponent_checker()) == True:
                ans.append(0)
            elif self.lookahead == 0:
                ans.append(50)
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_ans = opponent.scores_for(b)
                ans.append(100 - max(opponent_ans))
                b.remove_checker(col)
        return ans

    def next_move(self, b):
        """ overrides the next_move method in Player class
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)

#%%
def test():
    b = Board(6, 7)
    b.add_checkers('1211244445')
    print(AIPlayer('X', 'LEFT', 0).scores_for(b))
    print(AIPlayer('O', 'LEFT', 1).scores_for(b))
    print(AIPlayer('X', 'LEFT', 1).scores_for(b))
    print(AIPlayer('X', 'LEFT', 2).scores_for(b))
    print(AIPlayer('X', 'LEFT', 3).scores_for(b))
    print(AIPlayer('O', 'LEFT', 3).scores_for(b))
    print(AIPlayer('O', 'LEFT', 4).scores_for(b))

    print(AIPlayer('X', 'LEFT', 1).next_move(b))
    print(AIPlayer('X', 'RIGHT', 1).next_move(b))
    print(AIPlayer('X', 'LEFT', 2).next_move(b))
    print(AIPlayer('X', 'RIGHT', 2).next_move(b))
    print(AIPlayer('X', 'RANDOM', 2).next_move(b))

