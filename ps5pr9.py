# 
# ps5pr9.py - Problem Set 5, Problem 9
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#%%
def cube_all(values):
    """
    Raise each value in the values list to its cubic power
    return a new list containing all the cubes
    """
    results = []
    
    for i in range(len(values)):
        results.append(values[i] ** 3)
        
    return results



def test():
    """ performs test calls on the functions above """
    print(cube_all([-2, 5, 4, -3]))
    print(cube_all([1, 2, 3]))


#%%
def add_stars(s):
    """
    Inserts a star (*) between each character of the input string.
    """
    result = ''
    
    for i in range(len(s)):
        if i > 0:
            result = result + '*'
        result = result + s[i]
        
    return result


def test():
    """ performs test calls on the functions above """
    print(add_stars('hello'))
    print(add_stars('hangman'))
    print(add_stars('x'))
    
    
#%%
def compare(s1, s2):
    """
    Compares two strings and returns the count of differences 
    based on position and length.
    """
    result = 0
    len_shorter = min(len(s1), len(s2))
    
    for i in range(len_shorter):
        if s1[i] != s2[i]:
            result += 1
            
    result += abs(len(s1) - len(s2))
    return result


def test():
    """ performs test calls on the functions above """
    print(compare('alien', 'allen'))
    print(compare('alien', 'alone'))
    print(compare('aliens', 'alone'))


#%%
def weave(vals1, vals2):
    """
    Weaves two lists by alternating elements from each, 
    starting with the first list.
    If one list is longer, the remaining elements are appended to the end.
    """
    result = []
    len_shorter = min(len(vals1), len(vals2))
    
    for i in range(len_shorter):
        result += [vals1[i], vals2[i]]
        
    if len(vals1) > len_shorter:
        result += vals1[len_shorter:]
    elif len(vals2) > len_shorter:
        result += vals2[len_shorter:]
        
    return result


def test():
    """ performs test calls on the functions above """
    print(weave([1, 1, 1], [2, 2, 2]))
    print(weave([3, 4, 5, 6], [7, 8, 9, 0]))
    print(weave([0, 0, 0, 0], [1, 1]))
    print(weave([2, 1, 0], [3, 4, 5, 6]))
    print(weave([1, 2], []))
    print(weave([], [3, 4, 5]))
    print(weave([], []))
    
