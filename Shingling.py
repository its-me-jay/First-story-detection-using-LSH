import numpy as np
import binascii

#returns the shingles
def word_shingle(string):
    w=3
    words = string.split()
    num_words = len(words)

    if w > num_words or w == 0:
        print "Number of words are less than w"
        return [-1]
    return [[words[i] + " " + words[i + 1] + " " + words[i + 2]] for i in range(num_words - w + 1)]

#returns the 32 bit hash values of the shingles
def word_shingle_hashes(string):
    w=3
    words = string.split()
    num_words = len(words)

    if w > num_words or w == 0:
        print "Number of words are less than w"
        return [-1]
    #return [[words[i] + " " + words[i + 1] + " " + words[i + 2]] for i in range(num_words - w + 1)]
    return [binascii.crc32(words[i] + " " + words[i + 1] + " " + words[i + 2]) & 0xffffffff for i in range(num_words - w + 1)]

#Forms the shingle set with all shingles from a given set of documents. Here 'a' is an array of documents.
#The returned shingle set is a dictionary with keys = shingles and values = ids (0 to no.of shingles)
def formshingleSet(a):
    shingle_set={}
    count1 = 0
    count2=0
    for x in a:
        output = word_shingle_hashes(x)
        for i in output:
          if(i!=-1):
              try:
                  shingle_set[i]
              except:
                  shingle_set[i]=count2
                  count2+=1
              #shingle_set.add(crc)
        count1+=1
        print count1
    return shingle_set


#formshingleSet(a)
