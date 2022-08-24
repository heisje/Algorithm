rank = {'(': [0, 4],
        '+': [1, 1],
        '-': [2, 2],
        '*': [3, 3],
        '/': [3, 3],
        }

string = input() + ')'
s_opr = ['(']
postfix = []
first = True
numberrrrr = []
try:
    for temp in string:
        if temp == '-' and first is True:
            numberrrrr.append(temp)
        elif temp in ['(', '+', '-', '*', '/', ')']: #숫자가 아니면
            if len(numberrrrr) > 0:
                postfix.append(''.join(numberrrrr))
                numberrrrr = []
            if temp == ')':
                while True: # ( 나올때 까지 무한 pop
                    if s_opr[-1] == '(':
                        s_opr.pop()
                        break
                    else:
                        postfix.append(s_opr.pop())
            else:
                if temp == '(':
                    first = True
                if rank[temp][1] > rank[s_opr[-1]][0]: #새로 들어온게 더 크면
                    s_opr.append(temp)
                else: #작거나 같으면
                    while rank[temp][1] < rank[s_opr[-1]][0]:
                        postfix.append(s_opr.pop())
                    s_opr.append(temp)
        else: #숫자 면
            numberrrrr.append(temp)
            first = False
            #print(temp, end='')
    print(postfix)
    s_num = []
    for temp in postfix:
        if len(temp) == 2:
            s_num.append(int(temp))
        elif temp.isdigit():
            s_num.append(int(temp))
        else:
            num_2 = s_num.pop()
            num_1 = s_num.pop()
            if temp == '+':
                s_num.append(num_1 + num_2)
            elif temp == '-':
                s_num.append(num_1 - num_2)
            elif temp == '*':
                s_num.append(num_1 * num_2)
            elif temp == '/':
                s_num.append(num_1 // num_2)
    if len(s_num) == 1:
        print(*s_num)
    else:
        print("ROCK")
except:
    print("ROCK")




