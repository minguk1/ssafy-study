import requests
from pprint import pprint


def recommendation(title):

    find_URL = f"https://api.themoviedb.org/3/search/movie?api_key=8474173a15e459f15155e1769e2d8415&language=en-US&page=1&query={title}&include_adult=false"
    information = requests.get(find_URL).json() #찾고자 하는 제목을 링크에 넣어 그에 맞는 정보를 띄웠습니다.
    
    try:
        movie_id = information["results"][0]["id"] #찾은 정보에서 첫번째 영화의 id를 변수에 저장시킵니다.
    except IndexError: #이 때 에러가 발생하면
        return None #None을 반환하도록 해줍니다.

    URL = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=8474173a15e459f15155e1769e2d8415&language=Ko&page=1"#찾은 영화 id를 가지고 추천 영화 정보를 불러옵니다.
    response = requests.get(URL).json()
    recommend_movie_name = [] #추천 영화 정보들 중에 제목들만 리스트로 만들어주기 위해 빈 리스트를 미리 만들어 놓습니다.
    for i in response["results"]: #추천 영화 중에
        recommend_movie_name.append(i["title"]) #제목들만 만들어놓은 빈 리스트에 추가합니다.
    return recommend_movie_name
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
