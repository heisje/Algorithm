n = int(input())

final = []
while n >= 1:
    b = n % 2 #b = 나머지
    n = n // 2
    if b == 1:
        final.append('1')
    else:
        final.append('0')
    
print(''.join(final[::-1]))
    