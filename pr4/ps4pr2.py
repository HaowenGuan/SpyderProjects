#%% /Users/data/SpyderProjects/pr4/
from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

#%%
def pow_bin(b, e):
    base = bin_to_dec(b)
    exp = bin_to_dec(e)
    pow = dec_to_bin(base ** exp)
    return pow

#%%
pow_bin('11', '10')      # 3 ** 2 = 9
#%%
pow_bin('1001', '11')    # 9 ** 3 = 729

#%%
def smallest_bin(binvals):
    list_of_lists = [[bin_to_dec(b), b] for b in binvals]
    return min(list_of_lists)[1]

#%%
 smallest_bin(['1100', '110', '101', '10000'])