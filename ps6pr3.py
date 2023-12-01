#%%
def BUtify(s):
    result = ''
    for c in s:
        if c == 'b' or c == 'u':
            result += c.upper()
        else:
            result += c
    return result

# BUtify('you be you')
#%%
def diff(vals1, vals2):
    result = []
    shorter = min(len(vals1), len(vals2))
    for i in range(shorter):
        result += [abs(vals1[i] - vals2[i])]
    return result + vals1[shorter:] + vals2[shorter:]

diff([0, 3, 6, 9], [1, 1])