def line_test(line):
    pre_hight = line[0]
    flag = 0  # 내려가면 -1 올라가면 +1
    field_count = 1 #같은 수 지속 
    for i in range(1, len(line)):
        if pre_hight == line[i]:  # 같으면
            field_count += 1
            if fied
            pass
        else:  # 다른경우
            if pre_hight - line[i] == 1:  # 내려가요
                flag = -1
                field_count = 1
                pass
            elif pre_hight - line[i] == -1:  # 올라가요
                flag = 1
                field_count = 1
                pass
            else:
                # 두개이상 차이났을 때
                return 0
            field_count = 0

        

N, L = map(int, input().split())
arr = list(list(map(int, input().split()))for _ in range(N))

