# Name: Karthik and Vivian
# Date: 1/29/2020


filename = raw_input("Specify Filename: ")

# Read scores to a list, scoreList
scoreFile = open(filename, 'r')
scoreList = scoreFile.read().split()
scoreList = list(map(int, scoreList))

# Set total = 0
total = 0

# Set index counter(index) to 0
index = 0

# While the index is less than len(scoreList)

while index < len(scoreList):
    if index < (len(scoreList) - 3):
        if scoreList[index] == 10:
            total += scoreList[index] + scoreList[index + 1] + scoreList[index + 2]
            index += 1
        elif scoreList[index] + scoreList[index + 1] == 10:
            total += scoreList[index] + scoreList[index + 1] + scoreList[index + 2]
            index += 2

        else:
            total += (scoreList[index]+scoreList[index+1])
            index += 2

    else:
        if scoreList[index] == 10:
            total += scoreList[index] + scoreList[index + 1] + scoreList[index + 2]
            index += 3
            break

        elif scoreList[index] + scoreList[index + 1] == 10:
            total += scoreList[index] + scoreList[index + 1] + scoreList[index + 2]
            index += 3
            break

        else:
            total += scoreList[index] + scoreList[index + 1]
            index += 2
            break

print 'Final score: ', total
