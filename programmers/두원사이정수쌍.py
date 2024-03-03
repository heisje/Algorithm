from math import sqrt

def solution(r1, r2):
    quar = 0
    for i in range(0, r2):
        s1 = int(sqrt(max(0, r1**2 - i**2 - 1)))
        s2 = int(sqrt(r2**2 - i**2))
        quar += s2 - s1
    return quar * 4