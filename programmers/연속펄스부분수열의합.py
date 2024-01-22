#  0 1  2 3  4 5
# -1 1 -1 1 -1 1
#  1-1  1-1  1-1


def solution(sequence):
    save = []
    parse = -1
    
    save.append(sequence[0])
    
    for idx, s in enumerate(sequence[1:]):
        save.append(save[idx] + s * parse)
        parse *= -1
    
    mini = min(save)
    maxi = max(save)
    
    if mini >= 0 and maxi >= 0:
        return maxi
    if mini < 0 and maxi < 0:
        return -mini
    return abs(maxi) + abs(mini)
    