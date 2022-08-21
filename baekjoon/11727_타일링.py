#https://www.acmicpc.net/problem/11727
result_li = [0, 1]

N = int(input())
for n in range(2, N + 1):
    if len(result_li) <= n :
        if n % 2 == 1:
            result_li.append(result_li[n - 1] * 2 - 1)
        elif n % 2 == 0:
            result_li.append(result_li[n - 1] * 2 + 1)
print(result_li[N] % 10007)