# The main file containing all headlines
filemain = open(r"c:\\Users\Subh Chaturvedi\Documents\DS Projects\newpaper\headlines.txt","r+",encoding="utf-8")

#file1 = open(r"c:\\Users\Subh Chaturvedi\Documents\DS Projects\newpaper\headlinesLowerCase.txt","w+",encoding="utf-8")


# ALL THE HEADLINES
headLinesList = filemain.readlines()

# FUNCTION TO COUNT HEADLINES WHERE ANY OF THE WORD/S OCCURS
#   - wordsToSearch is a list of the form ["word1","word2","word3",...]
def countOccurancesAny(wordsToSearch):
    count = 0
    
    for headline in headLinesList:
        for eachWord in wordsToSearch:
            if headline.find(eachWord.lower()) != -1:
                count += 1
                break

    return count

# FUNCTION TO COUNT HEADLINES WHERE ANY OF THE WORD/S FROM MULTIPLE GROUPS OCCURS
#   - wordsToSearch is a list of lists, each of the form ["word1","word2","word3",...]
def countOccurancesGroupedAny(wordsToSearch):
    count = 0
    countMain = 0

    for headline in headLinesList:
        countMain = 0
        
        for eachGroup in wordsToSearch:
            optimiseCheck1 = 0

            for eachWord in eachGroup:
                if headline.find(eachWord.lower()) != -1:
                    optimiseCheck1 = 1
                    countMain += 1
                    break
            if optimiseCheck1 == 0:
                break
                
        if countMain == len(wordsToSearch):
            count += 1

    return count

# FUNCTION TO COUNT HEADLINES WHERE ALL OF THE WORD/S OCCURS
#   - wordsToSearch is a list of the form ["word1","word2","word3",...]
def countOccurancesAll(wordsToSearch):
    mainCount = 0
    wordCount = 0
    
    totalWords = len(wordsToSearch)

    for headline in headLinesList:
        wordCount = 0
        for eachWord in wordsToSearch:
            if headline.find(eachWord.lower()) == -1:
                break
            else:
                wordCount += 1
        if wordCount == totalWords:
            mainCount += 1

    return mainCount


# print(countOccurancesGroupedAny([["rape"],["uttar pradesh"]]))
# print(countOccurancesAll(["BJP","Congress","fight"]))
