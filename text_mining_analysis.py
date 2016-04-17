import string
import random


def proccessed_sonnet(fp):
    """
    cleans up the sonnets into just the sonnets in readable text without Roman numerals that had been
    used to label the sonnets 


    """
    lines = ""
	
    for line in fp.split("\n"):
		
		if line[1:len(line)].islower() == False:                    #taking out the roman numerals
			continue
		lines += line.strip(string.punctuation) +" " 
        
    return lines


#Markov Analysis

def process_file(fp):
    """
    places words and their frequency into a dictionary


    """
    hist = dict()
    for line in fp.split("\n"):
        process_line(line, hist)
    return hist

def process_line(line, hist):
    """
    splits line into words and takes out the punctuation and whitespace and finds
    the frequency of the words


    """
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

def random_word(h):
    """
    generates a random word based on the frequency that the words appear in Shakespeare's sonnets
    """
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)

def syllable(word):
    """
    counts the syllables in a word

    >>> syllable("apple")
    2
    >>> syllable(hippopotamus)
    5

    """
    count = 0

    vowels = ['a','e','i','o','u','y']
    dipthongs = ['oo','oi','ou','oi','oy','ea','ee', 'io']

    for letter in word:
        if letter in vowels:
            count += 1
    if word[-1] == "e":
        count -= 1
    if word[-2:] == "le":
        count += 1

    if count == 0:
        count += 1
    i = 0

    while i < len(word)-1:
        if word[i:i+2] in dipthongs:
            count -= 1
        i += 1


    return count

def line_syllable(line):
    """
    count syllables in line

    >>> print line_syllable("crackers are tasty")
    5



    """
    
    count = 0
    line = line.split(' ')

    for word in line:
        if len(word) > 0:
            count += syllable(word)
    return count

def Shakespeare(histogram):
    """
    takes words from the histogram of words from all of Shakespeare's 
    sonnets and puts them into the form of a Shakespearean sonnets

    """
    sonnet = []
    line = ""

    while len(sonnet) < 15:
        # print sonnet
        # print len(sonnet)
        while line_syllable(line) != 10:
            # print line
            word = random_word(histogram)
            if line_syllable(line + word) <= 10:
                # print 'a'
                line += word + " "
    
        sonnet.append(line)
        line = ""

    return sonnet

