# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 len 사용 금지
def title_length(movie):
    title_list = list(movie["title"]) #제목의 글자수를 세기 위해 글자 수별로 리스트를 나눴습니다.
    count = 0
    for i in title_list: #그 글자수의 리스트 원소마다 카운트를 세어 총 카운트를 반환하는 방법으로 하였습니다.
        count = count + 1
    return count
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(title_length(movie))  # 6 (공백 포함 길이)