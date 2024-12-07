XMASLENGTH = len("XMAS")
MASLENGTH = len("MAS")

def countXmasHorizontal(wordSearch, idxLine, idxChar):
    xmasCount = 0

    # XMAS
    if idxChar <= len(wordSearch[0]) - XMASLENGTH:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine][idxChar + 1]) +
                str(wordSearch[idxLine][idxChar + 2]) +
                str(wordSearch[idxLine][idxChar + 3]))
        if word == "XMAS":
            xmasCount += 1

    # SAMX
    if idxChar >= XMASLENGTH - 1:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine][idxChar - 1]) +
                str(wordSearch[idxLine][idxChar - 2]) +
                str(wordSearch[idxLine][idxChar - 3]))
        if word == "XMAS":
            xmasCount += 1

    return xmasCount

def countXmasVertical(wordSearch, idxLine, idxChar):
    xmasCount = 0

    # XMAS (top to bottom)
    if idxLine <= len(wordSearch) - XMASLENGTH:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine + 1][idxChar]) +
                str(wordSearch[idxLine + 2][idxChar]) +
                str(wordSearch[idxLine + 3][idxChar]))
        if word == "XMAS":
            xmasCount += 1

    # SAMX (top to bottom)
    if idxLine >= XMASLENGTH - 1:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine - 1][idxChar]) +
                str(wordSearch[idxLine - 2][idxChar]) +
                str(wordSearch[idxLine - 3][idxChar]))
        if word == "XMAS":
            xmasCount += 1

    return xmasCount

def countXmasDiagonalLeftRight(wordSearch, idxLine, idxChar):
    xmasCount = 0

    # XMAS (top to bottom)
    if idxChar <= len(wordSearch[0]) - XMASLENGTH and idxLine <= len(wordSearch) - XMASLENGTH:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine + 1][idxChar + 1]) +
                str(wordSearch[idxLine + 2][idxChar + 2]) +
                str(wordSearch[idxLine + 3][idxChar + 3]))
        if word == "XMAS":
            xmasCount += 1

    # SAMX (top to bottom)
    if idxChar >= XMASLENGTH - 1 and idxLine >= XMASLENGTH - 1:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine - 1][idxChar - 1]) +
                str(wordSearch[idxLine - 2][idxChar - 2]) +
                str(wordSearch[idxLine - 3][idxChar - 3]))
        if word == "XMAS":
            xmasCount += 1

    return xmasCount

def countXmasDiagonalRightLeft(wordSearch, idxLine, idxChar):
    xmasCount = 0

    # XMAS (top to bottom)
    if idxChar >= XMASLENGTH - 1 and idxLine <= len(wordSearch) - XMASLENGTH:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine + 1][idxChar - 1]) +
                str(wordSearch[idxLine + 2][idxChar - 2]) +
                str(wordSearch[idxLine + 3][idxChar - 3]))
        if word == "XMAS":
            xmasCount += 1

    # SAMX (top to bottom)
    if idxChar <= len(wordSearch[0]) - XMASLENGTH and idxLine >= XMASLENGTH - 1:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine - 1][idxChar + 1]) +
                str(wordSearch[idxLine - 2][idxChar + 2]) +
                str(wordSearch[idxLine - 3][idxChar + 3]))
        if word == "XMAS":
            xmasCount += 1

    return xmasCount

def countMasMas(wordSearch, idxLine, idxChar):
    if idxChar <= len(wordSearch[0]) - MASLENGTH and idxLine <= len(wordSearch) - MASLENGTH:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine + 1][idxChar + 1]) +
                str(wordSearch[idxLine + 2][idxChar + 2]) +
                str(wordSearch[idxLine][idxChar + 2]) +
                str(wordSearch[idxLine + 1][idxChar + 1]) +
                str(wordSearch[idxLine + 2][idxChar]))
        if word == "MASMAS":
            return 1
    return 0

def countMasSam(wordSearch, idxLine, idxChar):
    if idxChar <= len(wordSearch[0]) - MASLENGTH and idxLine <= len(wordSearch) - MASLENGTH:
        word = (str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine + 1][idxChar + 1]) +
                str(wordSearch[idxLine + 2][idxChar + 2]) +
                str(wordSearch[idxLine][idxChar + 2]) +
                str(wordSearch[idxLine + 1][idxChar + 1]) +
                str(wordSearch[idxLine + 2][idxChar]))
        if word == "MASSAM":
            return 1
    return 0

def countSamMas(wordSearch, idxLine, idxChar):
    if idxChar >= MASLENGTH - 1 and idxLine <= len(wordSearch) - MASLENGTH:
        word = (str(wordSearch[idxLine][idxChar - 2]) +
                str(wordSearch[idxLine + 1][idxChar - 1]) +
                str(wordSearch[idxLine + 2][idxChar]) +
                str(wordSearch[idxLine][idxChar]) +
                str(wordSearch[idxLine + 1][idxChar - 1]) +
                str(wordSearch[idxLine + 2][idxChar - 2]))
        if word == "SAMMAS":
            return 1
    return 0

def countSamSam(wordSearch, idxLine, idxChar):
    if idxChar <= len(wordSearch[0]) - MASLENGTH and idxLine >= MASLENGTH - 1:
        word = (str(wordSearch[idxLine - 2][idxChar]) +
                str(wordSearch[idxLine - 1][idxChar + 1]) +
                str(wordSearch[idxLine][idxChar + 2]) +
                str(wordSearch[idxLine - 2][idxChar + 2]) +
                str(wordSearch[idxLine - 1][idxChar + 1]) +
                str(wordSearch[idxLine][idxChar]))
        if word == "SAMSAM":
            return 1
    return 0

def part1(wordSearch):
    xmasCount = 0

    for idxLine in range(len(wordSearch)):
        for idxChar in range(len(wordSearch[0])):
            if str(wordSearch[idxLine][idxChar]) == "X":
                xmasCount += countXmasHorizontal(wordSearch, idxLine, idxChar)
                xmasCount += countXmasVertical(wordSearch, idxLine, idxChar)
                xmasCount += countXmasDiagonalLeftRight(wordSearch, idxLine, idxChar)
                xmasCount += countXmasDiagonalRightLeft(wordSearch, idxLine, idxChar)

    return xmasCount

def part2(wordSearch):
    xmasCount = 0

    for idxLine in range(len(wordSearch)):
        for idxChar in range(len(wordSearch[0])):
            if str(wordSearch[idxLine][idxChar]) == "M":
                xmasCount += countMasMas(wordSearch, idxLine, idxChar)
                xmasCount += countMasSam(wordSearch, idxLine, idxChar)
                xmasCount += countSamMas(wordSearch, idxLine, idxChar)
                xmasCount += countSamSam(wordSearch, idxLine, idxChar)

    return xmasCount

if __name__ == '__main__':
    file = open("inputs/day4.txt", "r")
    wordSearch = file.read().splitlines()

    answerPart1 = part1(wordSearch)
    print("Answer part 1: ", answerPart1)

    answerPart2 = part2(wordSearch)
    print("Answer part 2: ", answerPart2)
