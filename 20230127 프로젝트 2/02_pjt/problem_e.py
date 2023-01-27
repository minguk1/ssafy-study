import requests
from pprint import pprint


def credits(title):
    find_URL = f"https://api.themoviedb.org/3/search/movie?api_key=8474173a15e459f15155e1769e2d8415&language=en-US&page=1&query={title}&include_adult=false"
    information = requests.get(find_URL).json()
    
    try:
        movie_id = information["results"][0]["id"]
    except IndexError:
        return None
    
    URL = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8474173a15e459f15155e1769e2d8415&language=en-US" #d문제에서 했던 것 대신 출연진, 연출진 정보를 불러옵니다.
    response = requests.get(URL).json()
    cast_list = [] # 조건에 맞는 출연진과 연출진 이름들을 새로운 리스트에 넣기 위해 미리 만들어줍니다.
    directing_list = []

    for i in response["cast"]: # "cast"key의 value 리스트 안에서
        if int(i["cast_id"]) < 10: # cast id 가 10보다 작으면
            cast_list.append(i["name"]) #이름만 넣어줍니다.
    for i in response["crew"]: #"crew" key의 value 리스트 안에서
        if i["known_for_department"] == "Directing": #부서가 디렉팅이면
            directing_list.append(i["name"]) #이름만 넣어줍니다.
    directing_set = set(directing_list) #결과 형태처럼 중복을 피해주기 위해 세트로 바꿔주었습니다.
    result_dict = {} #결과 형식이 딕셔너리 형태라 새로 딕셔너리도 만들어줍니다.
    result_dict["cast"] = cast_list #차례대로 key 와 value를 다 입력 해주고
    result_dict["directing"] = directing_set
    return result_dict # 반환해줍니다.

    # recommend_movie_name = []
    # for i in response["results"]:
    #     recommend_movie_name.append(i["title"])
    # return recommend_movie_name
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
