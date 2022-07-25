N = int(input())

bag_5 = N // 5 #5g count
bag_3 = 0
for i in range(bag_5, -1, -1):
    #print(str(bag_5)+' '+str(bag_3))
    etc = N - 5 * i
    if etc % 3 == 0:
        bag_3 = etc // 3
        #print(str(i)+' '+str(bag_3))
        print(i+bag_3)
        break
else:
    print(-1)