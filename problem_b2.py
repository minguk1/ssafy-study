import json
from pprint import pprint


def movie_info(movie, genres):
    genre_name_list = []
    for i in range(len(genres_list)):
        if genres_list[i]["id"] in movie["genre_ids"]:
            genre_name_list.append(genres_list[i]["name"])
    movie["genre_name"] = genre_name_list
    result_dict = {}
    for i in movie:
        if i in ["id", "title", "poster_path", "vote_average", "overview", "genre_name"]:
            result_dict[i] = movie.get(i)

    
    return result_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
