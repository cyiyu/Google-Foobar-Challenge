from fractions import Fraction


def checkRadii(pegs, firstRadius):
    pointer = firstRadius
    for i in range(1, len(pegs)):
        disToNext = pegs[i] - pegs[i-1]
        nextRadius = disToNext - pointer
        if nextRadius < 1:
            return False
        pointer = nextRadius
    return True


def solution(pegs):
    even = len(pegs) % 2 == 0
    _sum = 0
    alternator = 2
    for item in pegs[1:len(pegs) - 1]:
        _sum += alternator*item
        alternator *= -1

    if even:
        _sum += (pegs[-1] - pegs[0])
        answer = Fraction(2*(float(_sum)/3)).limit_denominator()
    else:
        _sum += (-pegs[-1] - pegs[0])
        answer = Fraction(2*(float(_sum))).limit_denominator()
    answerDec = answer.numerator / answer.denominator
    radiusCheck = checkRadii(pegs, answerDec)
    if radiusCheck is False:
        return [-1, -1]
    else:
        return [answer.numerator, answer.denominator]
