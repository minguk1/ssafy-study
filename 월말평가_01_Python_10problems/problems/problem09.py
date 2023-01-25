# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    if number == 1:
        return str(1) #재귀함수의 종료 조건을 설정하였습니다. 1을 2로 나눈 나머지는 1
    return dec_to_bin(number//2)+str(number%2) #가장 처음 2로 나눈 나머지 계산값을 뒤로 넣어야하기 때문에 문자열로 바꿔주고 앞에 다시 함수를 붙였습니다.
    
    
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
