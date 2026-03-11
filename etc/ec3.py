# 5
# 5 2 3 2 5

_ = int(input())
li = list(map(int, input().split()))
result = 0
stack = [li[0]]

for i in li[1:]:
    while(True):
        if(len(stack) == 0 or i < stack[-1]):
            stack.append(i)
            break
        elif (i == stack[-1]):
            result += 1 
            break
        elif (i > stack[-1]):
            stack.pop()

print(result)