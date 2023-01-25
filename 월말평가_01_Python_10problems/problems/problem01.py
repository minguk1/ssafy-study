# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    sum_scores = sum(scores)  #sum함수를 이용해 리스트 내 점수들의 총합을 구해줍니다.
    avg_scores = sum_scores / len(scores) #len함수를 이용해 리스트 내 점수들의 개수를 계산하여 총합에서 나눠주면 그 값이 평균이 됩니다.
    return avg_scores
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5

#교수님 코드
def average(scores):
    sum_scores = sum(scores)  #sum함수를 이용해 리스트 내 점수들의 총합을 구해줍니다.
    avg_scores = sum_scores / len(scores) #len함수를 이용해 리스트 내 점수들의 개수를 계산하여 총합에서 나눠주면 그 값이 평균이 됩니다.
    return avg_scores