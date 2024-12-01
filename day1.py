def parseInputFile(file):
    leftList = []
    rightList = []

    file = file.read().splitlines()

    for line in file:
        newElemLeftList, newElemRightList = line.split("   ")
        leftList.append(int(newElemLeftList))
        rightList.append(int(newElemRightList))

    return leftList, rightList

def part1(leftList, rightList):
    totalDistance = 0

    leftList.sort()
    rightList.sort()

    for idx in range(len(leftList)):
        totalDistance += abs(leftList[idx] - rightList[idx])

    return totalDistance

def part2(leftList, rightList):
    scoreSimilarity = 0

    for leftElem in leftList:
        scoreSimilarity += leftElem * rightList.count(leftElem)

    return scoreSimilarity

if __name__ == '__main__':
    file = open("inputs/day1.txt", "r")
    leftList, rightList = parseInputFile(file)

    answerPart1 = part1(leftList, rightList)
    print("Answer part 1: ", answerPart1)

    answerPart2 = part2(leftList, rightList)
    print("Answer part 2: ", answerPart2)
