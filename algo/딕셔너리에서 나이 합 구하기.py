# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}, ]

age_sum = 0

for dict in infos:
    if "age" in dict:
        age_sum = age_sum + dict["age"]

print(age_sum)