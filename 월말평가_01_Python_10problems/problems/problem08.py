# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    word_list = list(word) #글자 하나하나 리스트로 변환하였습니다.
    
    number_list = []
    for i in word_list: #변환시킨 글자들 각각에 해당하는 아스키코드 숫자를 새로운 리스트로 저장하였습니다.
        word_number = ord(i)
        number_list.append(word_number)
    
    new_number_list = [] #변환시킨 숫자들을 n만큼 증가시키고 그 값이 소문자, 대문자를 구별하고 Z나 z를 넘어갈 때 값을 빼주었습니다.
    for j in number_list:
        if j >= 65 and j <= 90: # 대문자일 때
            if (j + n) > 90: # Z 넘어갈 때
                new_number = j + n - 26
            else:
                new_number = j + n
        if j >= 97 and j <= 122: # 소문자일 때
            if (j + n) > 122: # z 넘어갈때
                new_number = j + n - 26
            else:
                new_number = j + n
        
        new_number_list.append(new_number)

    new_word_list = "" #초기 문자 공백으로 설정하여
    for k in new_number_list:
        new_word_list = new_word_list + chr(k) #계산한 아스키코드 숫자에 해당하는 문자들을 하나씩 더해주었습니다.
    password = new_word_list #마지막 문자 리스트를 패스워드라는 변수로 설정

    return password
    
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
