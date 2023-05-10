from collections import deque

n = int(input())
sea = [0] * n
for i in range(n):
    sea[i] = list(map(int, input().split()))
    if 9 in sea[i]:
        r, c = i, sea[i].index(9) # 처음 상어 위치

size = 2
stack = 0
time = 0
total_time = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def upgrade_able(size, stack):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if 1 <= sea[i][j] < size:
                cnt += 1
    if cnt+stack < size:
        return False
    else:
        return True
def eat_able(size):
    for i in range(n):
        for j in range(n):
            if 1 <= sea[i][j] < size:
                return True
    return False

def eat_fish(i,j,size, stack, time):
    print("시작", time, i, j)
    global total_time

    visited = [[0]*n for _ in range(n)]
    visited[i][j] = 1
    q = deque()
    q.append((i,j))

    while q:
        r, c = q.popleft()
        # print(r,c, visited[r][c])
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if (0<=nr<n and 0<=nc<n) and visited[nr][nc]==0 and 1 <= sea[nr][nc] < size:
                print("먹음", nr, nc)
                stack += 1
                time = visited[r][c]
                total_time += time
                sea[nr][nc] = 0
                if stack == size:
                    print("진화")
                    stack = 0
                    size += 1
                    if eat_able(size) == True:

                        eat_fish(nr, nc, size, stack, time)
                        return
                    else:
                        print(time)
                        # print("end")
                        return time
                else:
                    if eat_able(size) == True:
                        print("더먹기가능")
                        print(time, "time")

                        eat_fish(nr, nc, size, stack, time)
                        return
                    else:

                        print(time)
                        return time
            elif (0<=nr<n and 0<=nc<n) and visited[nr][nc]==0 and (sea[nr][nc] == 0 or sea[nr][nc] == size):
                time += 1
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
                # print("append")

eat_fish(r,c,2,0,0)
print(total_time, "최종시간")