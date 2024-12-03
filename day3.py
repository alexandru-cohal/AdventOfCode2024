import re

def calcSumMultipl(sequence):
    sumMultipl = 0

    for multiplication in re.findall("mul\([0-9]+,[0-9]+\)", sequence):
        terms = re.findall("[0-9]+", multiplication)
        sumMultipl += (int(terms[0]) * int(terms[1]))

    return sumMultipl

def part1(memory):
    return calcSumMultipl(memory)

def part2(memory):
    sumMultipl = 0

    memory = "do()" + memory + "don't()"

    doSequences = re.split("do\(\)", memory)
    for sequence in doSequences:
        doDontSequences = re.split("don't\(\)", sequence)

        sumMultipl += calcSumMultipl(doDontSequences[0])

    return sumMultipl

if __name__ == '__main__':
    file = open("inputs/day3.txt", "r")
    memory = file.read()

    answerPart1 = part1(memory)
    print("Answer part 1: ", answerPart1)

    answerPart2 = part2(memory)
    print("Answer part 2: ", answerPart2)
