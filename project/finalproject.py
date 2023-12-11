#%%
# Final Project
#
# Writing style analysis model
#
import math

class TextModel:
    def __init__(self, model_name):
        """ constructor for TextModel class """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        # Chosen feature: first words of sentences
        self.sentence_first_words = {}

    def __repr__(self):
        """ Return a string representation of the TextModel. """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of sentence first words: ' + str(len(self.sentence_first_words))
        return s
    
    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces
            to all of the dictionaries in this text model.
        """
        words = clean_text(s)
        for word in words:
            # words counts
            if word not in self.words:
                self.words[word] = 0
            self.words[word] += 1
            # word lengths counts
            if len(word) not in self.word_lengths:
                self.word_lengths[len(word)] = 0
            self.word_lengths[len(word)] += 1
            # stems counts
            word_stem = stem(word)
            if word_stem not in self.stems:
                self.stems[word_stem] = 0
            self.stems[word_stem] += 1
        # sentence lengths counts
        sentences = s.replace('?', '.').replace('!', '.').lower()
        sentences = sentences.split('.')
        sentences.pop()  # remove last empty sentence
        for sentence in sentences:
            sentence = clean_text(sentence)
            if len(sentence) not in self.sentence_lengths:
                self.sentence_lengths[len(sentence)] = 0
            self.sentence_lengths[len(sentence)] += 1
        # sentence first words counts
        for sentence in sentences:
            words = clean_text(sentence)
            if len(words) > 0:
                word = words[0]
                if word not in self.sentence_first_words:
                    self.sentence_first_words[word] = 0
                self.sentence_first_words[word] += 1


    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)

    def save_model(self):
        """ saves the TextModel object self by writing feature dictionaries to files """
        f = open(self.name + '_words', 'w')
        f.write(str(self.words))
        f.close()
        f = open(self.name + '_word_lengths', 'w')
        f.write(str(self.word_lengths))
        f.close()
        f = open(self.name + '_stems', 'w')
        f.write(str(self.stems))
        f.close()
        f = open(self.name + '_sentence_lengths', 'w')
        f.write(str(self.sentence_lengths))
        f.close()
        f = open(self.name + '_sentence_first_words', 'w')
        f.write(str(self.sentence_first_words))
        f.close()

    def read_model(self):
        """ reads the stored dictionaries """
        f = open(self.name + '_words', 'r')
        d_str = f.read()
        f.close()
        self.words = dict(eval(d_str))
        f = open(self.name + '_word_lengths', 'r')
        d_str = f.read()
        f.close()
        self.word_lengths = dict(eval(d_str))
        f = open(self.name + '_stems', 'r')
        d_str = f.read()
        f.close()
        self.stems = dict(eval(d_str))
        f = open(self.name + '_sentence_lengths', 'r')
        d_str = f.read()
        f.close()
        self.sentence_lengths = dict(eval(d_str))
        f = open(self.name + '_sentence_first_words', 'r')
        d_str = f.read()
        f.close()
        self.sentence_first_words = dict(eval(d_str))

    def similarity_scores(self, other):
        """ computes and returns a list of log similarity scores of self and other """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        sentence_first_words_score = compare_dictionaries(other.sentence_first_words, self.sentence_first_words)
        return [word_score, word_lengths_score, stems_score, sentence_lengths_score, sentence_first_words_score]
    
    def classify(self, source1, source2):
        """ Compares source1 and source2 to see which of these is the more 
            likely source of the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ': ' + str(scores1))
        print('scores for ' + source2.name + ': ' + str(scores2))
        sum1 = sum(scores1)
        sum2 = sum(scores2)
        print(source1.name + ' vs ' + source2.name + ': ' + str(sum1) + ' vs ' + str(sum2))
        if sum1 > sum2:
            print(self.name + ' is more likely to have come from ' + source1.name)
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)

def stem(s):
    """ returns the stem of s """
    if s.endswith('ies'):
        return s[:-3] + 'i'
    elif s.endswith('s') and not s.endswith('ss'):
        return s[:-1]
    elif s.endswith('ing') and len(s) > 4:
        return s[:-3]
    elif s.endswith('ed') and len(s) > 3:
        return s[:-2]
    elif s.endswith('er') and len(s) > 3:
        return s[:-2]
    elif s.endswith('est') and len(s) > 4:
        return s[:-3]
    elif s.endswith('ly') and len(s) > 3:
        return s[:-2]
    else:
        return s


def clean_text(txt):
    """ cleans txt of all punctuation and returns a list of words in txt """
    txt = txt.lower()
    for symbol in """.,?"'!;:""": # remove punctuation
        txt = txt.replace(symbol, '')
    return txt.split()


def compare_dictionaries(d1, d2):
    """ compares the two dictionaries d1 and d2 and returns their log similarity score """
    if d1 == {}:
        return -50
    score = 0
    total = 0
    for key in d1:
        total += d1[key]
    for key in d2:
        if key in d1:
            score += d2[key] * math.log(d1[key] / total)
        else:
            score += d2[key] * math.log(0.5 / total)
    return score


def run_tests():
    """ My test function """
    source1 = TextModel('sheldon')
    source1.add_file('sheldon_source_text.txt')

    source2 = TextModel('leonard')
    source2.add_file('leonard_source_text.txt')

    sheldon_test = TextModel('sheldon_test')
    sheldon_test.add_file('sheldon_test_text.txt')
    sheldon_test.classify(source1, source2)

    leonard_test = TextModel('leonard_test')
    leonard_test.add_file('leonard_test_text.txt')
    leonard_test.classify(source1, source2)

    belle = TextModel('belle')
    belle.add_file('belle_test_text.txt')
    belle.classify(source1, source2)

    beast = TextModel('beast')
    beast.add_file('beast_test_text.txt')
    beast.classify(source1, source2)

