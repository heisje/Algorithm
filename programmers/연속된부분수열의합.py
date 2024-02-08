def solution(sequence, k):
    N = len(sequence)

    max_sum = 0
    start = 0
    end = 0
    interval = N

    for start in range(N):
        while max_sum < k and end < N:
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end-1-start < interval:
            res = [start, end-1]
            interval = end-1-start
        max_sum -= sequence[start]

    return res