from harddata.nameLength import nameLength
from harddata.startingLetter import startingLetter
from harddata.wordEnds import wordEnds
from harddata.chunks import ternChunk
import random
import re

def wRandFrmDct(dct):
    rand_val = random.randint(1, sum(dct.values()))
    total = 0
    for k, v in dct.items():
        total += v
        if rand_val <= total:
            return k
    assert False, 'unreachable'

def nameGenerator():
    length = wRandFrmDct(nameLength)
    print(length)
    firstLetter = wRandFrmDct(startingLetter)
    pseudoCityName = ''
    paredChunk = {}

    # Assign
    for k,v in ternChunk.items():
        if re.match(r"^{}".format(firstLetter), k):
            if k in paredChunk:
                paredChunk[k] += 1
            else:
                paredChunk[k] = 1
            paredChunk[k] += v
    # print(paredChunk)
    pseudoCityName += wRandFrmDct(paredChunk)
    paredChunk = {}
    print(pseudoCityName)

    for i in range(2,int(length)-1): # run this code up until it fills the length of the word
        for k,v in ternChunk.items():
            if re.match(r"{}$".format(pseudoCityName[-2:]), k):
                if k in paredChunk:
                    paredChunk[k] += 1
                else:
                    paredChunk[k] = 1
                paredChunk[k] += v
        pseudoCityName += wRandFrmDct(paredChunk)
        print(pseudoCityName)

        #TODO:look at final two letters in pseudoCityName and compare to first two letters of chunk
        #TODO:weighted-randomly select from that pared list and append the final character to the pseudoCityName variable

    #TODO:once two chars from end of word, append a weighted triple from wordEnds dictionary based on one overlapping letter
        # return pseudoCityName

# for k,v in ternChunk.items():
#     var = 'ce'
#     if re.match(r"^{}".format(var), k):
#         print(k,v)

nameGenerator()
