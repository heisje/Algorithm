# 공유기의 거리를 구해야하는데
# 거리를 1씩 늘리기에는 숫자가 너무 크다
# 최소거리, 최대거리를 잡은 뒤에
# 이진탐색으로 거리를 찾는다.
# 거리를 찾는 방법은, 브루트포스로 전부 돈다.
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
li = [int(input()) for _ in range(N)]
li.sort()

def binarySearch(left, right):
    answer = 0
    
    while left <= right:
        center = (left + right) // 2
        #print(left, right, center)

        current = li[0]
        count = 1

        for i in range(len(li)):
            if li[i] >= center + current:
                count += 1
                current = li[i]
            if count >= C:
                break
        
        if count >= C:
            # 거리를 더 늘릴 수 있음, 답으로 가능성이 있음
            answer = center
            left = center + 1
        if count < C:
            # 거리를 더 줄여야함, 불가능
            right = center - 1

    return answer

left = 1
right = li[-1] - li[0]
print(binarySearch(left, right))