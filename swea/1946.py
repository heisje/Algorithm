testcase_len = int(input())
for testcase in range(testcase_len):
    line_len = int(input())
    print(f'#{testcase+1}')
    all = ""
    for line in range(line_len):
        alpabet, repeat = input().split()
        all += alpabet * int(repeat)
    line_max = (len(all) // 10) 
    line = 0
    while line <= line_max:
        if line == line_max:
            print(all[line * 10 : ])
        else:
            print(all[line * 10 : line * 10 +10])
        line = line + 1