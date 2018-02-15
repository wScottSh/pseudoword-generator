import citylist
import random
cityList = citylist.citylist

# cityList = ['amazing', 'determine', 'foraging']

def writeDictionary(list):
    chunkyDict = {}
    firstLetterDict = {}
    nameLengthDict = {}
    wordEnds = {}

    for word in list:
        wordEndFreq(word, wordEnds)
        # chunkFreq(word, chunkyDict)
        # firstLetterFreq(word, firstLetterDict)
        # nameLengthFreq(word, nameLengthDict)
    # print(chunkyDict)
    print(wordEnds)
    # print(firstLetterDict)
    # print(nameLengthDict)

def wordEndFreq(word, wordEnds):
    for i in range(len(word), len(word)+1):
        end = word[i-3:i].lower()
        if end in wordEnds:
            wordEnds[end] += 1
        else:
            wordEnds[end] = 1

def chunkFreq(word, chunkyDict):
    for i in range(3, len(word)+1):
        chunk = word[i-3:i].lower()
        if chunk in chunkyDict:
            chunkyDict[chunk] += 1
        else:
            chunkyDict[chunk] = 1

def firstLetterFreq(word, firstLetterDict):
    firstLetter = word[0].lower()
    if firstLetter in firstLetterDict:
        firstLetterDict[firstLetter] += 1
    else:
        firstLetterDict[firstLetter] = 1

def nameLengthFreq(word, nameLengthDict):
    nameLength = str(len(word))
    if nameLength in nameLengthDict:
        nameLengthDict[nameLength] += 1
    else:
        nameLengthDict[nameLength] = 1

writeDictionary(cityList)

# Don't know how this works at all!
# class WeightedRandomizer:
#     def __init__(self, weights):
#         self.__max = .0
#         self.__weights = []
#         for value, weight in weights.items():
#             self.__max += weight
#             self.__weights.append((self.__max, value))
#
#     def random(self):
#         r = random.random() * self.__max
#         for ceil, value in self.__weights:
#             if ceil > r: return value
#
# w = {'A': 1.0, 'B': 1.0, 'C': 18.0}
#
# wr = WeightedRandomizer(w)
#
# results = {'A': 0, 'B': 0, 'C': 0}
# for i in range(10000):
#     results [wr.random()] += 1
#
# print('After 10000 rounds the distribution is:')
# print(results)
#
# # How to sort a dict by value (Python 2.4 or greater):
# for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
#     print "%s: %s" % (key, value)
