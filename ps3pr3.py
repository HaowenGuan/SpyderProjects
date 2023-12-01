#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
#

# A template for the first function that you are required to write.
def rotate(c, n):
    """ your docstring goes here """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)
        
    # Put the rest of your code for this function below.
    if 'a' <= c <= 'z':
        x = ord(c) - ord('a')
        y = x + n
        if y >= 26:
            y = y - 26
        z = chr(y + ord('a'))
    elif 'A' <= c <= 'Z':
        x = ord(c) - ord('A')
        y = x + n
        if y >= 26:
            y = y - 26
        z = chr(y + ord('A'))
    else:
        z = c
    return z


#### Put your code for the encipher function below. ####

def encipher(s, n):
    assert(type(s) == str)
    if s == '':
        return ''
    output = rotate(s[0], n) #hello, s[0] -> 'h', s[1:] -> ello
    return output + encipher(s[1:], n)


# A helper function that you will use in implementing your 
# string_score function.
# You should *NOT* modify this function.
def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': 
        return 0.1904
    elif c == 'e' or c == 'E': 
        return 0.1017
    elif c == 't' or c == 'T': 
        return 0.0737
    elif c == 'a' or c == 'A': 
        return 0.0661
    elif c == 'o' or c == 'O': 
        return 0.0610
    elif c == 'i' or c == 'I': 
        return 0.0562
    elif c == 'n' or c == 'N': 
        return 0.0557
    elif c == 'h' or c == 'H': 
        return 0.0542
    elif c == 's' or c == 'S': 
        return 0.0508
    elif c == 'r' or c == 'R': 
        return 0.0458
    elif c == 'd' or c == 'D': 
        return 0.0369
    elif c == 'l' or c == 'L': 
        return 0.0325
    elif c == 'u' or c == 'U': 
        return 0.0228
    elif c == 'm' or c == 'M': 
        return 0.0205
    elif c == 'c' or c == 'C': 
        return 0.0192
    elif c == 'w' or c == 'W': 
        return 0.0190
    elif c == 'f' or c == 'F': 
        return 0.0175
    elif c == 'y' or c == 'Y': 
        return 0.0165
    elif c == 'g' or c == 'G': 
        return 0.0161
    elif c == 'p' or c == 'P': 
        return 0.0131
    elif c == 'b' or c == 'B': 
        return 0.0115
    elif c == 'v' or c == 'V': 
        return 0.0088
    elif c == 'k' or c == 'K': 
        return 0.0066
    elif c == 'x' or c == 'X': 
        return 0.0014
    elif c == 'j' or c == 'J': 
        return 0.0008
    elif c == 'q' or c == 'Q': 
        return 0.0008
    elif c == 'z' or c == 'Z': 
        return 0.0005
    else:
        return 0.0

#%%
#### Put your code for string_score and decipher below. ####
def string_score(s):
    assert(type(s) == str)
    if s == '':
        return 0
    output = letter_score(s[0])
    return output + string_score(s[1:])

#%%
def decipher(s):
    assert(type(s) == str)
    options = [encipher(s, n) for n in range(0, 26)]
    scored_strs = [[string_score(s), s] for s in options]
    best_str = max(scored_strs)
    return best_str[1]
    
# #%%
# decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj')
# #%%
# decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.')
# #%%
# decipher('python')

