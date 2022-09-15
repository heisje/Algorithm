N = int(input())
M = int(input())
arr = input()
find = 'I' + 'OI' * N

count = 0
i = 0
trg = False
trg_count = 0
count = 0
while i < M:
    if trg is False:
        if arr[i] == 'I':
            trg = True
        i += 1
    if trg is True:
        if arr[i:i+2] == 'OI':
            trg_count += 1
            i += 2
        else:
            trg = False
            trg_count = 0
        
        if trg_count >= N :
            count += 1   

print(count)