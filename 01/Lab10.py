# 세개의 정수 숫자를 입력받고 가장 큰 숫자를 출력하는 프로그램
# 첫 번째 숫자 입력받기
inputNumber1 = int(input("첫 번째 숫자를 입력하세요: "))
# 두 번째 숫자 입력받기
inputNumber2 = int(input("두 번째 숫자를 입력하세요: "))
# 세 번째 숫자 입력받기
inputNumber3 = int(input("세 번째 숫자를 입력하세요: "))
# 가장 큰 숫자를 판별하기
maxNumber = max(inputNumber1,inputNumber2,inputNumber3)
# 출력하기
print("가장 큰 숫자는", maxNumber,"입니다.")