# 가장 처음 같은 것이 나온 위치를 찾아야함
R, C = map(int, input().split())
DATA = [list(input()) for n in range(R)]
rotate_data = ['' for _ in range(C)]
for c in range(C):
    for r in range(R):
        rotate_data[c] += DATA[r][c]

l, r = 0, C-1
answer = 0
while l <= r:
    mid = (l + r) // 2

    # mid일 때, 뒤의 문자열저장
    sameFlag = False
    checker = set()
    for c in range(C):
        string = rotate_data[c][mid:R]
        if string in checker:
            # 실패
            sameFlag = True
            break
        else:
            checker.add(string)
            continue
    
    if sameFlag:
        r = mid - 1
    else:
        l = mid + 1

print(r)