testcase = int(input())

total_max = 0 #전체 합
for testcase_num in range(testcase):
    a_len, b_len = input().split()
    a_len = int(a_len)
    b_len = int(b_len)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    match_len = 0
    match_count = 0
    if a_len > b_len:
        match_len = a_len - b_len + 1
        c = a
        a = b
        b = c
        match_count = b_len
    else:
        match_len = b_len - a_len + 1
        match_count = a_len
    total_max = 0
    for i in range(match_len):
        sub_max = 0
        for j in range(match_count):
            sub_max += a[ j ] * b[ i + j ]
        if sub_max > total_max:
            total_max = sub_max
    print(f'#{testcase_num+1} {total_max}')
