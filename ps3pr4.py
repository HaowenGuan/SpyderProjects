# ps3pr4.py (Problem Set 3, Problem 4)

def first_occur(elem, seq):
    # Base Case I, if seq is empty, elem is not in seq, so return -1
    if len(seq) == 0:
        return -1
    # Base Case II, if elem == the first element in seq, return 0
    if elem == seq[0]:
        return 0
    # Recursively search rest of seq
    index = first_occur(elem, seq[1:])
    # If recersion return is not -1, it is found in the subarray, 
    # so add 1 for the current array as result
    if index >= 0:
        index = index + 1
    return index

# #%%
# first_occur(5, [4, 10, 5, 3, 7, 5])
# #%%
# first_occur('hi', ['well', 'hi', 'there'])
# #%%
# first_occur('b', 'banana')
# #%%
# first_occur('a', 'banana')
# #%%
# first_occur('i', 'team')
# #%%
# first_occur('hi', ['hello', 111, True])
# #%%
# first_occur('a', '')      # the empty string
# #%%
# first_occur(42, [])       # the empty list

#%%
def rem_first(c, s):
    # Base Case I, if s is empty, elem is not in s, so return ''
    if len(s) == 0:
        return ''
    # Base Case II, if c == the first character in s, remove it and return the rest of substring
    if c == s[0]:
        return s[1:]
    # Recursively search rest of s
    output = rem_first(c, s[1:])
    return s[0] + output

# #%%
# rem_first('a', 'bananas')
# #%%
# rem_first('n', 'bananas')
# #%%
# rem_first('x', 'bananas')    # no occurrences
# #%%
# rem_first('a', '')

#%%
def jscore(s1, s2):
    # Two Base Cases, either s1 or s2 is empty, we return 0
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[0] in s2:
            jscore_rest = jscore(s1[1:], rem_first(s1[0], s2))
            return jscore_rest + 1
        else:
            jscore_rest = jscore(s1[1:], s2)
            return jscore_rest

# #%%
# jscore('diner', 'syrup')            # just the 'r'
# #%%
# jscore('always', 'bananas')         # two 'a's and one 's'
# #%%
# jscore('always', 'walking')         # one 'a', 'l', and 'w'
# #%%
# jscore('recursion', 'excursion')    # everything but the 'r' in s1 is shared by s2
# #%%
# jscore('recursion', '')
# #%%
# jscore('', 'recursion')

#%%
def negate_last(n, values):
    # Base Case I, if values is empty, n is not found in values
    if len(values) == 0:
        return []
    # Base Case II, if n == the last element in values, it is found
    # We remove the last elment and return the rest of values list
    if n == values[-1]:
        values[-1] = values[-1] * -1
        return values
    return negate_last(n, values[:-1]) + [values[-1]]

# #%%
# negate_last(3, [2, 3, 1, 2, 3, 4])
# #%%
# negate_last(2, [2, 3, 1, 2, 3, 4])
# #%%
# negate_last(7, [9, 5, 7, 7, 7])
# #%%
# negate_last(2, [1, 3, 5, 7, 9])    # no occurrences
# #%%
# negate_last(2, [])
