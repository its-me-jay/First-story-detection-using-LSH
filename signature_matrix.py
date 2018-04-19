import shingling
import time
import random
import math
import numpy as np

#immediate prime after the total no.of shingles. 
nextPrime = 1607923

with open("stories.txt",'r') as f:
    a=f.readlines()

a=[x.strip() for x in a]

shingle_set=shingling.formshingleSet(a)
maxShingleID = len(shingle_set)

def pickRandomCoeffs(k):
    randList = []
    while k > 0:
        randIndex = random.randint(0, maxShingleID)
        while randIndex in randList:
          randIndex = random.randint(0, maxShingleID)
        randList.append(randIndex)
        k = k - 1
    return randList

numHashes = 100 #no. of rows in signature matrix
coeffA = pickRandomCoeffs(numHashes)
coeffB = pickRandomCoeffs(numHashes)

def form_signature_matrix(shingle_set,a):
    #signature_matrix=np.array([])
    signature_matrix=[]
    doc=0
    for i in range(len(a)):
        shingles=shingling.word_shingle_hashes(a[i])
        if(shingles[0]!=-1):
            #sig_column=np.array([])
            sig_column=[]
            for p in range(numHashes):
                sig_value=float("inf")
                for k in shingles:
                    hash_value = (coeffA[p]*shingle_set[k] + coeffB[p]) % nextPrime
                    if(hash_value<sig_value):
                        sig_value=hash_value
                #sig_column=np.append(sig_column,sig_value)
                sig_column.append(sig_value)
            #signature_matrix=np.append(signature_matrix,sig_column)
            signature_matrix.append(sig_column)
        doc+=1
        print doc

    #signature_matrix=np.resize(signature_matrix,(len(signature_matrix)/100,100))
    return signature_matrix

t1=time.time()
signature_matrix=form_signature_matrix(shingle_set,a)
t2=time.time()
print t2-t1
