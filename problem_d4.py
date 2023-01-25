import json


def max_revenue(movies):
    id_list = []
    for i in range(len(movies_list)):
        id_list.append(movies_list[i]["id"])

    revenue_dict = {}    
    for d in id_list:
        Movie = open(f'data/movies/{d}.json', encoding='utf-8')
        movies_detail_list = json.load(Movie)
        revenue_dict[movies_detail_list["revenue"]] = movies_detail_list["title"]

    for k in revenue_dict:
        if k == max(revenue_dict):
            return revenue_dict[k]
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    max_revenue(movies_list)
    print(max_revenue(movies_list))

# id_list = []
# for i in range(len(movies_list)):
#     id_list.append(movies_list[i]["id"])
# print(id_list)

# revenue_dict = {}
# for d in id_list:
#     Movie = open(f'data/movies/{d}.json', encoding='utf-8')
#     movies_detail_list = json.load(Movie)
#     revenue_dict[movies_detail_list["revenue"]] = movies_detail_list["title"]


# print(revenue_dict)

# print(max(revenue_dict))

# for k in revenue_dict:
#     if k == max(revenue_dict):
#         return revenue_dict[k]