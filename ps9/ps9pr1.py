#%%
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """ initialize Board
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        # add dashes at the bottom of the board
        s += '-' * (self.width * 2 + 1)
        s += '\n'

        # and the numbers underneath the dashes
        for i in range(self.width):
            s += ' ' + str(i % 10)
        s += '\n'

        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    
    ### add your reset method here ###
    
    def add_checkers(self, columns):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: columns is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in columns:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here

    def reset(self):
        """ reset the Board to empty spaces
        """
        self.slots = [[' '] * self.width for row in range(self.height)]


    def can_add_to(self, col):
        """ returns True if we can place a checker in the column col
        """
        if col < 0 or col >= self.width or self.slots[0][col] != ' ':
            return False
        return True
    

    def is_full(self):
        """ returns True if the Board is completely full of checkers
        """
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True
    

    def remove_checker(self, col):
        """ removes the top checker from column col
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    
    def is_win_for(self, checker):
        """ returns True if there are four consecutive checker
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) or \
            self.is_vertical_win(checker) or \
            self.is_down_diagonal_win(checker) or \
            self.is_up_diagonal_win(checker):
            return True
        return False

    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                    return True
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                    return True
        return False
    

#%%
def test():
    b = Board(6, 7)
    print(b)
    b.add_checker('X', 0)
    b.add_checker('O', 0)
    b.add_checker('X', 0)
    b.add_checker('O', 3)
    b.add_checker('O', 6) 
    print(b)
    b2 = Board(3, 3)
    b2.add_checkers('0200')
    print(b2)
    b = Board(6, 7)
    b.add_checkers('00102030')
    print(b)
    print(b.is_win_for('X'))
    print(b.is_win_for('O'))
    b2 = Board(6, 7)
    b2.add_checkers('23344545515')
    print(b2)
    print(b2.is_win_for('X'))
    print(b2.is_win_for('O'))

