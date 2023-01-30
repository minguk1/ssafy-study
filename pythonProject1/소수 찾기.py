N = int(input())


a_list = list(map(int, input().split()))

result_list = []
for a in a_list:
    if a%2 == 0 or a==1:
        result_list.append(0)
        print(result_list)
    else:
        for b in range(2, a):
            if a%b == 0:
                result_list.append(0)
                break
            else:
                pass
            # result_list.append(1)
        print(result_list)

result = N - len(result_list)
print(result)