T = int(input())

for p in range(1, T+1):


    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    e = 0
    # print(a[0], b[0])
    k = 0
    while k<abs(N-M)+1:
        d = 0
        for i in range(0, min(N,M)):
            if N >= M:

                c = a[i+k] * b[i]
            else :
                c = a[i] * b[i + k]

            d = d + c

        # print((d))
        # print(sum(d))
        if d >= e:
            e = d
        k = k+1
    # print(e)
    print(f"#{p} {e}")