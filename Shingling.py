import numpy as np

with open("stories.txt",'r') as f:
    a=f.readlines()
a=[x.strip() for x in a]

def word_shingle(string, w):

    words = string.split()
    num_words = len(words)

    if w > num_words or w == 0:
        print "Number of words are less than w"
        return

    return [words[i:i + w] for i in range(num_words - w + 1)]

def character_shingle(string, w):

    characters = list(string)
    num_characters = len(characters)

    if w > num_characters or w == 0:
        print "Number of words are less than w"

    return [characters[i:i + w] for i in range(num_characters - w + 1)]

shingle_set = []

def formshingleSet(a):
    count1 = 0
    for x in a:
        shingles = word_shingle(x,3)
        if(count1==0):
            shingle_set = shingles
        else:
            shingle_set = np.append(shingle_set,shingles)
        print "status",count1
        count1+=1

formshingleSet(a)
shingle_set = np.resize(shingle_set,(3,len(shingle_set)/3))
print len(shingle_set)
