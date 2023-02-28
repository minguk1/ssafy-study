from itertools import combinations


n = int(input())
space = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    space[i] = [x, y]

johap = list(combinations(space, int(n/2)))

print(space)
print(johap)
min_sum = 9999999999999999
for i in johap:
    # print(i[0])
    x_sum = 0
    y_sum = 0
    for j in range(n//2):
        x_sum += i[j][0]
        y_sum += i[j][1]
    for k in range(n//2):
        if space[k] not in i:
            print(i)
            print(space[k])
            x_sum -= space[k][0]
            y_sum -= space[k][1]
            print(x_sum, y_sum)
    if x_sum*x_sum+y_sum*y_sum < min_sum:

        min_sum = x_sum*x_sum+y_sum*y_sum


print(min_sum)