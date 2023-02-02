six_list = []
k = 0
for i in range(1,100012135135153):
    if "666" in str(i):
        six_list.append(i)
        k += 1
        if k == 10000:
            break

t = int(input())
print(six_list[t-1])