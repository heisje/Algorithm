N = int(input())

def a(b):
    c = str(b)
    if '666' in c:
        return b
    else:
        return 0

print(list(range(0, N*1000)))
b = list(map(a, list(range(0, N*1000))))
print(sorted(b))

