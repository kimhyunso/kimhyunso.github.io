n, m, k = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))


max_target = max(numbers)
numbers.remove(max_target)
result = 0

for i in range(1, m + 1):
    if i % (k + 1) == 0:
        result += max(numbers)
    else:
        result += max_target
        
print(result)







