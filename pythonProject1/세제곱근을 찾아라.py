T = int(input())
for tc in range(1, T + 1):

    n = int(input())
    result = False
    # print(int(n ** 0.5))
    # print(n**0.5)
    for p in range(int(n ** 0.5), int(n ** 0.25) -1 , -1):
        if int(n / p) == p ** 2:
            result = True
            break
        if int(n / p) > int(p ** 2):
            break
    if result == True:

        print(f"#{tc} {p}")
    else:
        print(f"#{tc} -1")