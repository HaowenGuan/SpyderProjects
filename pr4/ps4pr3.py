#%%
def double_rec(binvals):
    if len(binvals) == 0:
        return []
    cur = binvals[0] + '0'
    return [cur] + double_rec(binvals[1:])

#%%
double_rec(['1100', '10011', '101', '010'])
#%%
double_rec(['01', '100', '11'])

#%%
def double_lc(binvals):
    binvals = [b + '0' for b in binvals]
    return binvals

#%%
double_rec(['1100', '10011', '101', '010'])
#%%
double_rec(['01', '100', '11'])

#%%
def add_bitwise(b1, b2):
    # Base cases
    if not b1:
        return b2
    if not b2:
        return b1

    # Calculate the sum of the bits
    total = int(b1[-1]) + int(b2[-1])

    # Determine the result bit based on the total
    if total == 2:
        # If there's a carry, we need to add '1' to the sum of the remaining bits
        return add_bitwise(add_bitwise(b1[:-1], '1'), b2[:-1]) + '0'
    else:
        return add_bitwise(b1[:-1], b2[:-1]) + str(total)

#%%
print(add_bitwise('11', '100'))  # '111'
#%%
print(add_bitwise('11', '1'))  # '100'
#%%
print(add_bitwise('', '101'))  # '101'
#%%
print(add_bitwise('11100', '11110'))  # '111010'


#%%