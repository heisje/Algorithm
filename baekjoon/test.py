numbers = [1,1,3,12,123,23,12,12,12,3,0,1,1]

save_end = '_'
i = 0
while i < len(numbers):
    if save_end == numbers[i]:
        numbers.pop(i)
    else: 
        save_end = numbers[i]
        i += 1

print(numbers)