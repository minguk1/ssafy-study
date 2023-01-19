#
# T = int(input()) #T=3
#
# for i in range(1, T+1):


n = int(input())
J = []
K = []
for m in range(0, n):
    J.append(list(map(int, input().split())))

    print(J[m])
print(J)
# 세로로 출력할 때
# K = sorted(J, reverse=True)
# for i in range(n):
#     J[0][i] = K[0][i]
#     print(J[0][i])

for i in range(n):
    for j in range(n):
        k = n-1-j
        K[i].append(J[k][i])
print(J)
# for k in range(n):
#     for i in range(n):
#         print(J[k][i])

# for i
