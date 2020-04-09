import math


def findDivisors(x, l):
    n = l[x]
    divList = []
    for i in range(1, int((math.sqrt(n) + 1))):
        if n % i == 0:
            if i in l:
                # divList += [i for j in range(l[:x+1].count(i))]
                divList += [p for p, q in enumerate(l[:x + 1]) if q == i]
            if n / i in l and (n / i) != i:
                divList += [p for p, q in enumerate(l[:x + 1]) if q == (n / i)]
    return sorted(divList)


def makeDivDict(l):
    divDict = {}
    for i in range(len(l)):
        divDict[i] = findDivisors(i, l)
    return divDict


def solution(l):
    if len(l) < 3:
        return 0
    divDict = makeDivDict(l)
    count = 0
    for i in range(len(l) - 1, 1, -1):
        listDiv = divDict[i]
        for j in range(len(listDiv) - 2, -1, -1):
            listDiv2 = divDict[int(listDiv[j])]
            count += len(listDiv2) - 1
    return count


print solution([1, 2, 2, 4])
