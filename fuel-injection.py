def solution(n):
    n = int(n)
    ans = 0
    while True:
        if n == 3:
            n -= 1
            ans += 1
            continue
        if n == 1:
            return ans
        if n & 1 == 0:
            n /= 2
        else:
            if ((n - 2) & (n - 1)) < (n & (n + 1)):
                n -= 1
            else:
                n += 1
        ans += 1


print solution('15')
