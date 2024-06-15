T = int(input())
 
for test_case in range(1, T + 1):
    end = input()
    start = input()
    stack = [start]
    answer = 'No'
    while stack:
        text = stack.pop()
        if text == end:
            answer = 'Yes'
            break
        #if text not in end:
        #    continue
        if len(text) < len(end):
            continue
        if text[-1] == 'X':
            stack.append(text[:-1])
        if text[0] == 'Y':
            stack.append(text[1:][::-1])
    print(f'#{test_case} {answer}')