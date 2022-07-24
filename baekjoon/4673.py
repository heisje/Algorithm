def ad(n):
    sum = n
    while n > 0:
        digit = n % 10
        n = (n - digit)//10
        sum += digit
    return sum

dic = {i:False for i in range(1, 10001)}
for key, value in dic.items():
    sum = ad(key)
    if sum < 10001:
        dic[sum] = True

for key, value in dic.items() :
    if value == False:
        print(key)
