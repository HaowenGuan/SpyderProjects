#%%
def dec_to_bin(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    if n % 2 == 1:
        cur = '1'
    else:
        cur = '0'
    return dec_to_bin(n // 2) + cur

# #%%
# dec_to_bin(5)
# #%%
# dec_to_bin(12)
# #%%
# dec_to_bin(0)

#%%
def bin_to_dec(b):
    if b == '0':
        return 0
    if b == '1':
        return 1
    if b[-1] == '1':
        cur = 1
    else:
        cur = 0
    return bin_to_dec(b[:-1]) * 2 + cur

#%%
bin_to_dec('101')
#%%
bin_to_dec('1100')
#%%
bin_to_dec('0')

#%%
