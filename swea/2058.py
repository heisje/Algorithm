a = int(input())
b = 0
 
while a >= 1:
    b += a % 10
    a = (a - a % 10)/ 10
     
print(int(b))