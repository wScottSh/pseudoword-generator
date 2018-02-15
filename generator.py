from harddata.nameLength import nameLength
from harddata.startingLetter import startingLetter
from harddata.wordEnds import wordEnds
from harddata.chunks import ternChunk
import random
import re

def wRandFrmDct(dct): # define function that takes a dictionary
    rand_val = random.randint(1, sum(dct.values()))   # pulls in a random number from the random module and assigns it to rand_val
    total = 0                    # creates a running total and defults it to 0
    for k, v in dct.items():     # pulls the key and value tuple from the dictionary
        total += v               # adds the value of each key to the total variable (this is creating the weighted-ness)
        if rand_val <= total:    # if the random input is <= to total (this is the issue, need to normalize first)
            return k
    assert False, 'unreachable'

def nameGenerator():
    length = wRandFrmDct(nameLength)
    firstLetter = wRandFrmDct(startingLetter)
    pseudoCityName = ''

    #TODO:look at all the keys in dct that start with the firstLetter var and append that triple to the pseudoCityName

    for i in range(1, length-2): # run this code up until it fills the length of the word
        #TODO:look at final two letters in pseudoCityName and compare to first two letters of chunk
        #TODO:weighted-randomly select from that pared list and append the final character to the pseudoCityName variable

    #TODO:once two chars from end of word, append a weighted triple from wordEnds dictionary based on one overlapping letter
        return pseudoCityName

for k,v in ternChunk.items():
    
    if re.match(r"^la", k):
        print(k,v)
