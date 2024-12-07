import re

def parseInputFile(file):
    rulesSection = True
    ruleList = []
    updateList = []

    for line in file.read().splitlines():
        if rulesSection:
            if line == "":
                rulesSection = False
                continue
            else:
                # Page ordering rules
                pages = re.split("\|", line)
                ruleList.append([int(pages[0]), int(pages[1])])
        else:
            # Updates
            update = [int(page) for page in re.split(",", line)]
            updateList.append(update)

    return ruleList, updateList

def fixUpdate(ruleList, update):
    updateOrdered = False

    while not updateOrdered:
        updateOrdered = True

        for rule in ruleList:
            try:
                idxLeft = update.index(rule[0])
                idxRight = update.index(rule[1])
            except:
                continue
            else:
                if idxLeft > idxRight:
                    updateOrdered = False
                    update[idxLeft], update[idxRight] = update[idxRight], update[idxLeft]
                    break

    return update

def part1part2(ruleList, updateList):
    sumMidUpdateOrdered = 0
    sumMidUpdateFixed = 0

    for update in updateList:
        updateOrdered = True

        for rule in ruleList:
            try:
                idxLeft = update.index(rule[0])
                idxRight = update.index(rule[1])
            except:
                continue
            else:
                if idxLeft > idxRight:
                    update = fixUpdate(ruleList, update)
                    updateOrdered = False
                    break
        if updateOrdered:
            sumMidUpdateOrdered += update[int((len(update) - 1) / 2)]
        else:
            sumMidUpdateFixed += update[int((len(update) - 1) / 2)]

    return sumMidUpdateOrdered, sumMidUpdateFixed

if __name__ == '__main__':
    file = open("inputs/day5.txt", "r")
    ruleList, updateList = parseInputFile(file)

    answerPart1, answerPart2 = part1part2(ruleList, updateList)
    print("Answer part 1: ", answerPart1)

    print("Answer part 2: ", answerPart2)
