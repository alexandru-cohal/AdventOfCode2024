def parseInputFile(file):
    reportsList = []
    file = file.read().splitlines()

    for line in file:
        reportsList.append([int(elem) for elem in line.split(" ")])

    return reportsList

def getDirection(a, b):
    return b > a
    # TRUE means an increasing direction, FALSE means a decreasing direction

def checkReportSafe(report):
    directionReport = getDirection(report[0], report[1])

    for idxReport in range(len(report) - 1):
        if not ((1 <= abs(report[idxReport] - report[idxReport + 1]) <= 3) and
                (directionReport == getDirection(report[idxReport], report[idxReport + 1]))):
            return 0
    return 1

def checkReportSafeWithTolerance(report):
    oneBadLevelTolerance = True
    directionReport = getDirection(report[0], report[1])

    for idxReport in range(len(report) - 1):
        if not ((1 <= abs(report[idxReport] - report[idxReport + 1]) <= 3) and
                (directionReport == getDirection(report[idxReport], report[idxReport + 1]))):
            elemListEliminateLeft = report.copy()
            elemListEliminateLeft.pop(idxReport)

            elemListEliminateRight = report.copy()
            elemListEliminateRight.pop(idxReport + 1)

            if checkReportSafe(elemListEliminateLeft) or checkReportSafe(elemListEliminateRight):
                return 1
            else:
                return 0

    return 1

def part1(reportsList):
    safeReportCount = 0

    for report in reportsList:
        safeReportCount += checkReportSafe(report)

    return safeReportCount

def part2(reportsList):
    safeReportCount = 0

    for report in reportsList:
        if checkReportSafeWithTolerance(report) or checkReportSafe(report[1:]):
            safeReportCount += 1

    return safeReportCount

if __name__ == '__main__':
    file = open("inputs/day2.txt", "r")
    reportsList = parseInputFile(file)

    answerPart1 = part1(reportsList)
    print("Answer part 1: ", answerPart1)

    answerPart2 = part2(reportsList)
    print("Answer part 2: ", answerPart2)
