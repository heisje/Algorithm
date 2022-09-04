from math import sqrt

def dfs(n, N, count):
    global mini
    if count >= 4:
        return
    if n == 0:
        if count < mini:
            mini = count
        print(count)
        return 
    for i in range(int(sqrt(n)),0,-1):
        count += 1
        n=n-int(sqrt(i))**2
        dfs(n, N, count)
        count -= 1
    pass

N = int(input())
result = [] 
mini = 5
dfs(N, N, 0)
print(mini)

'''
for n in range(int(math.sqrt(N)), 0, -1):
    count = 0 
    while N > 0 or count > 4:
        print(int(math.sqrt(N)), N-int(math.sqrt(N))**2)
        N=N-int(math.sqrt(N))**2
        count += 1
        if N == 0:
            break
'''