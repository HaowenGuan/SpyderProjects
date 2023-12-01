#%%
# ps8pr2.py  (Problem Set 8, Problem 2)
#
#  Markov text generation
#

def create_dictionary(filename):
    """ takes the name of a text file and builds a dictionary
    """
    # read in the file as one big string    
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    lines = text.split('.')
    lines = [line + '.' for line in lines if len(line) > 0]
    
    # start with an empty dictionary
    d = {}
    
    for line in lines:
        words = line.split()
        prev = '$'
        for w in words:
            if prev not in d:
                d[prev] = []
            d[prev].append(w)
            prev = w
    return d

# #%%
# word_dict = create_dictionary('sample.txt')
# word_dict
# #%%
# word_dict = create_dictionary('edited_mission.txt')
# word_dict
# #%%
# word_dict = create_dictionary('brave.txt')
# word_dict

#%%
import random

def generate_text(word_dict, num_words):
    """Generate a random text based on the word_dict
    """
    cur = '$'
    for _ in range(num_words):
        if cur not in word_dict:
            cur = '$'
        next_word = random.choice(word_dict[cur])
        print(next_word, end=' ')
        cur = next_word

# word_dict = create_dictionary('sample.txt')
# print(word_dict)
# generate_text(word_dict, 20)




# %%
a = list(range(100))
# %%
