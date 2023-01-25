# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over_24(people):
    count = 0 #카운트를 위해 count = 0 이라는 초기값 설정
    for i in people: #people이라는 리스트 내 딕셔너리 i 에 대해
        if i["age"] > 24: #i의 age value 값이 24 초과이면
            count = count + 1   #count 가 증가하도록 설정하고 총 카운트를 반환하도록 하였습니다.
    return count

    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4