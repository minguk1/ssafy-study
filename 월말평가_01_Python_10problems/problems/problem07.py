# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    numbers_list = list(numbers) #입력한 숫자들의 개수를 세기 위해 리스트 형식으로 변환시켰습니다.
    if len(numbers_list) == 1: #입력한 숫자들이 1개일 때
        pi = 3.14
        return numbers_list[0]**2*pi #원의 넓이 계산값 반환
    elif len(numbers_list) == 2: #입력한 숫자들이 2개일 때
        if (numbers_list[0] + numbers_list[1]) % 2 == 1: #또한 입력한 숫자 두 개의 합이 홀수일 때
            return numbers_list[0]*numbers_list[1]/2 # 삼각형 넓이 반환
        else: #아니면 짝수일 때
            return numbers_list[0]*numbers_list[1] #사각형 넓이 반환
    elif len(numbers_list) >= 3: #입력한 숫자 개수가 3개 이상일 때
        numbers_sum = sum(numbers_list) #합의 변수 설정
        numbers_avg = sum(numbers_list)/len(numbers_list) #평균의 변수 설정
        return (numbers_sum, numbers_avg,) #합의 변수, 평균의 변수 순으로 튜플 반환
        # 여기에 코드를 작성하여 함수를 완성합니다.
    else: #입력 개수가 0이라면 0 반환
        return 0

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0