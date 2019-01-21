def countWords(textfile, stopwords):
    emptydic = {}
    openfile = open(textfile, "r")
    stoplist = readStopWords(stopwords)
    for line in openfile:
        list = line.split()
        for i in range(len(list)):
            if list[i] not in stoplist:
                if list[i] not in emptydic:
                    emptydic[list[i]] = 1
                else:
                    emptydic[list[i]] = emptydic[list[i]] + 1
            else:
                emptydic = emptydic
    return emptydic

def printTop20(dic):
    sorteddic = sorted(dic.items(), key=lambda kv: kv[1], reverse = True)
    top20 = sorteddic[0:20]
    for pair in top20:
        print(pair[0] + " = " + str(pair[1]))

def readStopWords(textfile):
    openfile = open(textfile, "r")
    wordlist = []
    for line in openfile:
        word = line.strip()
        wordlist.append(word)
    return wordlist

def similarity(textfile1, textfile2, stopwords):
    wordcountTxt1 = countWords(textfile1, stopwords)
    txt1keys = wordcountTxt1.keys()
    wordcountTxt2 = countWords(textfile2, stopwords)
    txt2keys = wordcountTxt2.keys()
    wordoverlap = 0
    for word in txt1keys:
        if word in txt2keys:
            wordoverlap += 1
        else:
            wordoverlap = wordoverlap
    similarityScore = wordoverlap / (len(wordcountTxt1) + len(wordcountTxt2) - wordoverlap)
    print(similarityScore)
