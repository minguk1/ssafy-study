# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    max_score = 0 #최고점수는 0점 이상이기 때문에 초기값을 0점으로 잡아주었습니다.
    min_score = 100 #최저점수는 100점 이하이기 때문에 초기값을 100점으로 잡아주었습니다.
    for i in scores:
        if i >= max_score:
            max_score = i #리스트 내 점수들에 대하여 그 점수가 최고점수 설정값보다 크면 그 점수가 최고점수가 되게 설정하였습니다.
        else:
            max_score = max_score #리스트 내 점수가 최고점수보다 크지 않다면 최고점수가 유지되도록 설정하였습니다.
    for j in scores:
        if i <= min_score:
            min_score = j #리스트 내 점수들에 대하여 그 점수가 최저점수 설정값보다 작으면 그 점수가 최저점수가 되게 설정하였습니다.
        else:
            min_score = min_score  # 리스트 내 점수가 최저점수보다 작지 않다면 최저 점수가 유지되도록 설정하였습니다.
    return (min_score, max_score,) #튜플 형태로 반환
    
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
