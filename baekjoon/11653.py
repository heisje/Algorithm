import sys
a = int(sys.stdin.readline().rstrip())
if a == 1:
    print(1)
i = 2
while a > 1:
    if a % i == 0:
        a = a // i
        print(i)
        i = 2
    else : 
        i += 1

        
        
