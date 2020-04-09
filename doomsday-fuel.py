import numpy as np
from fractions import Fraction


def getN(trans, term, m):
    m_1 = np.delete(m, term, 0)
    Q = np.delete(m_1, term, 1)
    I_t = np.identity(len(trans))
    N_in = np.subtract(I_t, Q)
    N = np.linalg.inv(N_in)
    return N


def getR(trans, term, m):
    m_1 = np.delete(m, term, 0)
    m_2 = np.delete(m_1, trans, 1)
    return m_2


def solution(m):
    for i in range(len(m)):
        s = sum(m[i])
        for j in range(len(m)):
            if sum(m[i]):
                m[i][j] = float(m[i][j]) / s
    trans = []
    term = []
    i = 0
    for row in m:
        if sum(row):
            trans.append(i)
        else:
            term.append(i)
        i += 1
    if sum(m[0]) == 0:
        ansZero = [0]*(len(term)+1)
        ansZero[0] = 1
        ansZero[-1] = 1
        return ansZero
    R = getR(trans, term, m)
    N = getN(trans, term, m)
    B = np.matmul(N, R)
    B_0 = B[0]
    ansFrac = [Fraction(entry).limit_denominator() for entry in B_0]
    lcm = np.lcm.reduce([int(frac.denominator) for frac in ansFrac])
    ans = [0] * (len(ansFrac) + 1)
    ans[-1] = int(lcm)
    for i in range(len(ansFrac)):
        num = ansFrac[i].numerator
        den = ansFrac[i].denominator
        if den == lcm:
            ans[i] = int(num)
        else:
            factor = lcm / den
            ans[i] = int(num * factor)
    return ans


sol = solution([[0]])
# for item in sol:
#     print item
print sol
