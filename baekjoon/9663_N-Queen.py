def solve(y, N):
    global result
    if y == N:
        result += 1
        return
    if vi_c_lt[x+y] < N-y or vi_c_rt[y-x+N] < N-y:
        return
    for x in range(N):  # x축 하나를 선택한다.
        # 선택해보았는데, visited에 아직 선택 안했으면 pass
        if vi_x[x] == 0 and vi_c_lt[x+y] == 0 and vi_c_rt[y-x+N] == 0:
            vi_x[x] = vi_c_lt[x+y] = vi_c_rt[y-x+N] = 1
            solve(y+1, N)
            vi_x[x] = vi_c_lt[x+y] = vi_c_rt[y-x+N] = 0


N = int(input())
result = 0
vi_x = [0] * N
vi_c_lt = [0] * (N*2+1)
vi_c_rt = [0] * (N*2+1)
solve(0, N)
print(f'{result}')

# 골드