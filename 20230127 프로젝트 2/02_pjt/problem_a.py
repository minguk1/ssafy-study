import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=8474173a15e459f15155e1769e2d8415&language=en-US&page=1'
    response = requests.get(URL).json()
    return len(response["results"]) #불러온 response 딕셔너리에서 result에 해당하는 value list를 추출하여 원소 개수를 len으로 세어 줍니다.
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
