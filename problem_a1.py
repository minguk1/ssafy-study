import json
from pprint import pprint


def movie_info(movie):
    result_dict = {}
    for i in movie:
        if i in ["id", "title", "poster_path", "vote_average", "overview", "genre_ids"]:
            result_dict[i] = movie.get(i)
    return result_dict

# pprint(movie_info(movie))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


