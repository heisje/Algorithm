def solution(arr):

    def quad(w, x, y):
        if w > 1:
            nxtW = w//2
            q1 = quad(nxtW, x, y)
            q2 = quad(nxtW, x + nxtW, y)
            q3 = quad(nxtW, x, y + nxtW)
            q4 = quad(nxtW, x + nxtW, y + nxtW)

            if q1 == q2 == q3 == q4:
                if w == N:
                    answer[q1] += 1
                return q1
            for i in [q1, q2, q3, q4]:
                answer[i] += 1
            return 2
        return arr[y][x]

    N = len(arr)
    answer = [0, 0, 0]
    quad(N, 0, 0)
    return [answer[0], answer[1]]
