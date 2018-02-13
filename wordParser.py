import citylist

cityList = [ 'Neo',
  'Max Tessenholtz',
  'Marcy Lina',
  'Christopher Hanten',
  'Jorge Rodriguez',
  'Aleena Madni',
  'Tess Craig',
  'Jake Chavez',
  'Scott Sheppard',
  'Lillian Chernin' ]

def writeDictionary(list):
    chunky = {}
    firstLetters = {}
    for word in list:
        chunkFreq(word, chunky)
        firstLetterFreq(word, firstLetters)
    print(chunky)
    print(firstLetters)

def chunkFreq(word, chunky):
    for i in range(3, len(word)+1):
        chunk = word[i-3:i].lower()
        if chunk in chunky:
            chunky[chunk] += 1
        else:
            chunky[chunk] = 1

def firstLetterFreq(word, firstLetters):
    firstLetter = word[0].lower()
    if firstLetter in firstLetters:
        firstLetters[firstLetter] += 1
    else:
        firstLetters[firstLetter] = 1

def nameLengthFreq:
    pass # add functionality here

writeDictionary(cityList)
