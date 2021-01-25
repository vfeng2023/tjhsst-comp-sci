# Name: Vivian Feng and Shriya Muthukumar
# Date: 2.21.2020

# repurposed for lab 24 into function
def createFontDict():
    # create dictionary
    stateCodes = {}
    # read file for state codes
    codeList = open('postalCodes.txt', 'r').readlines()

    stateIndex = 0
    while stateIndex < len(codeList):
        stateCodes[codeList[stateIndex].strip()] = codeList[stateIndex + 1].strip()  # {abbreviation: state}
        stateIndex += 2

    # read file for state pop and create dict
    popList = open('population.txt', 'r').readlines()

    popDict = {}
    for line in popList:
        contents = line.split()
        popDict[contents[0]] = int(contents[1])  # convert population to string, {stateAbbrev: pop}

    # assign pop to font
    # min font  = 12, max font = 50
    minFont, maxFont = 12, 50
    minPop = min(popDict.values())
    maxPop = max(popDict.values())
    # assign to each state state abbreviation to name
    fontDict = {}
    for abbrev in popDict.keys():
        statePop = popDict[abbrev]
        scaledFont = int((statePop - minPop) * (maxFont - minFont) / float(maxPop - minPop) + minFont)
        stateName = stateCodes[abbrev]
        fontDict[stateName] = scaledFont

    return fontDict


"""Code below for testing purposes"""

# stateFonts = open('stateFonts.txt','w')
# fontDict = createFontDict()
# sortedStates = sorted(fontDict.keys())
# for state in sortedStates:
#     print state,fontDict[state]
#     stateFonts.write(state + " " + str(fontDict[state]) + "\n")
