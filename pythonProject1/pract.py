N = 4
A = [[0]*4 for _ in range(N)]
print(A)
A[0][0] = 1
i = 0
j = 0
change_count = N - 1
k = 0
p = 1

while True:
    if p == N ** 2 + 1:
        break
    if k == change_count:
        k = 0
        break
    else:
        k += 1
        p += 1
        j += 1
        A[i][j] = p

print(A)
print(p)
print(i, j)
print(k)
while True:
    if p == N ** 2 + 1:
        break
    if k == change_count:
        k = 0
        break
    else:
        k += 1
        p += 1
        i += 1
        A[i][j] = p

print(A)
print(i)
print(j)
print(p)
while True:
    if p == N ** 2 + 1:
        break
    if k == change_count:
        k = 0
        change_count -= 1
        break
    else:
        k += 1
        p += 1
        j -= 1
        A[i][j] = p
print(A)
print(i)
print(j)
print(p)
while True:
    if p == N ** 2 + 1:
        break
    if k == change_count:
        k = 0
        break
    else:
        k += 1
        p += 1
        i -= 1
        A[i][j] = p
print(A)
print(i)
print(j)
print(p)

while True:
    if p == N ** 2 + 1:
        break
    if k == change_count:
        k = 0
        break
    else:
        k += 1
        p += 1
        j += 1
        A[i][j] = p
print(A)
print(i)
print(j)
print(p)

while True:
    if p == N ** 2 + 1:
        break

    if k == change_count:
        k = 0
        break
    else:
        k += 1
        p += 1
        i += 1
        if A[i][j] > 0:
            k -= 1
            p -= 1
            i -= 1
            break
        A[i][j] = p
print(A)
print(i)
print(j)
print(p)
while True:
    if p == N ** 2 + 1:
        break
    if k == change_count:
        k = 0
        change_count -= 1
        break
    else:
        k += 1
        p += 1
        j -= 1
        if A[i][j] > 0:
            k -= 1
            p -= 1
            j += 1
            break
        A[i][j] = p
print(A)
print(i)
print(j)
print(p)
