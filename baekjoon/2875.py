n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
max = 0

if n >= 2 * m: #그룹을 짤 때 여성이 더 많은 경우
    max = m
    wait_k = n - (m * 2)
    while k - wait_k > 0:
        max -= 1
        k -= 3
elif n < 2 * m: #그룹을 짤 때 남성이 더 많은 경우
    max = n // 2
    wait_k = m - (n // 2)
    if n % 2 == 1:
        wait_k += 1
    while k - wait_k > 0:
        max -= 1
        k -= 3

print(max)
#28