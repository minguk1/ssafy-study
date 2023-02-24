T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    #입력 받으면서 물 개수 세 주기
    cnt = 0
    Arr = [0] * n
    for i in range(n):
        t = input()
        cnt += t.count("W")
        Arr[i] = list(t)

    # print(cnt, Arr)
    #물 개수만큼 리스트 미리 만들어주고 좌표 입력받기
    water = [0] * cnt
    idx = 0
    for i in range(n):
        for j in range(m):
            if Arr[i][j] == "W":
                water[idx] = [i, j]
                idx += 1
            if idx == cnt:
                break
        if idx == cnt:
            break
    # print(water)
    #이제 행렬 돌면서 L 마다 W까지의 최소 거리 리스트에 담고
    # dis_Arr = [[0]*m for _ in range(n)]
    # print(dis_Arr)
    dis_sum = 0
    for i in range(n):
        for j in range(m):
            if Arr[i][j] == "L":
                distance = n*m
                for k in water:
                    if abs(i-k[0]) + abs(j-k[1]) < distance:
                        distance = abs(i-k[0]) + abs(j-k[1])
                dis_sum += distance

    # print(dis_Arr)
    # 합 구해주기

    print(f"#{tc} {dis_sum}")