num = 0

try:
    num = int(input("숫자를 입력해주세요."))
    print("try가 실행되는지 확인")
except ValueError:
    print("값 에러 발생")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
print(num)