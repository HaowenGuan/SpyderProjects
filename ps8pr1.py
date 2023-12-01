#
# ps8pr1.py  (Problem Set 8, Problem 1)
#
# A class to represent calendar dates       
#
from copy import deepcopy

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def days_in_month(self):
        """ Returns the number of days in the called object's month
        """
        numdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            numdays[2] = 29
            
        return numdays[self.month]    

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def day_name(self):
        """ Return the day of the week that the called Date object falls on. 
            IMPORTANT: This method won't work until you implement the 
            other methods of the class, as specified in Problem 1.
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        monday = Date(11, 20, 2023)
        num_days = self.days_between(monday)
        return day_names[num_days % 7]
    
    #### Put your code for the methods from Problem 1 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
    
    def advance_one(self):
        """ advance one calendar day
        """
        if self.day == self.days_in_month():
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        else:
            self.day += 1
    
    def __eq__(self, other):
        """Return True if two dates represent the same calendar date
        """
        if self.month == other.month and self.day == other.day and self.year == other.year:
            return True
        else:
            return False
    
    def is_before(self, other):
        """Return True if self date comes before other date
        """
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False
    
    def is_after(self, other):
        """Return True if self date comes after other date
        """
        if self.__eq__(other) or self.is_before(other):
            return False
        return True
    
    def days_between(self, other):
        """Compute the number of day between two date
        """
        if self.is_after(other):
            date1 = deepcopy(other)
            date2 = deepcopy(self)
            sign = 1
        else:
            date1 = deepcopy(self)
            date2 = deepcopy(other)
            sign = -1
        counter = 0
        while date1 != date2:
            date1.advance_one()
            counter += 1
        return sign * counter
    
    
    
    
def test():
    d1 = Date(11, 19, 2023)
    print(d1.month)
    print(d1.day)
    print(d1.year)
    d = Date(12, 31, 2023)
    print(d)
    d.advance_one()
    print(d)
    d = Date(2, 28, 2024)
    print(d)
    d.advance_one()
    print(d)
    d.advance_one()
    print(d)
    d.advance_one()
    print(d)
    d1 = Date(1, 1, 2024)
    d2 = d1
    d3 = d1.copy()
    print(d1 == d2)
    print(d1 == d3)
    d1 = Date(11, 17, 2023)
    d2 = Date(12, 21, 2023)
    print(d2.days_between(d1))
    print(d1.days_between(d2))
    print(d1)
    print(d2)
    d3 = Date(12, 1, 2019)
    d4 = Date(3, 15, 2020)
    print(d4.days_between(d3))
    # 8)
    d = Date(11, 19, 2023)
    print(d.day_name())
    print(Date(11, 21, 2023).day_name())
    print(Date(1, 1, 2100).day_name())
    print(Date(7, 4, 1776).day_name())
    
    
    
    
    
    
    
    
    
    
    
    
    