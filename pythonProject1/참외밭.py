n = int(input())
input_dict = {}
input_list = []
for i in range(6):
    a, b = map(int, input().split())
    input_list.append(a)
    input_list.append(b)
    if a in input_dict:
        input_dict[a] = input_dict.get(a,[])+[b]
    else:
        input_dict[a] = [b]
print(input_list)
print(input_dict)
total_space = 1

for i in input_dict:
    if input_list.count(i) == 1:
        total_space = total_space * input_dict[i][0]
print(total_space)

