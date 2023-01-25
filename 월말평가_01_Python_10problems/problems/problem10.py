# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    x = position[0] #x의 초기위치
    y = position[1] #y의 초기위치
    dx = [-1, 1, 0, 0] #M값에 따른 x 방향 설정
    dy = [0, 0, -1, 1] #M값에 따른 y 방향 설정
    x = x + dx[M] #M값에 따른 방향으로 이동하고 난 뒤 x 위치
    y = y + dy[M] #M값에 따른 방향으로 이동하고 난 뒤 y 위치
    if x < 0 or x > N or y < 0 or y > N: #x나 y가 게임 캐릭터 공간 벗어 났을 때 조건
        return False
    else :
        return True
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
