# 소득 금액을 입력받고 소득세를 계산하는 프로그램
# 소득세 계산 함수
def calculate_tax(income):
    # 1만불이하의 경우
    if income < 10000:
        result = str(income*0.1)
    # 1만불초과　2만불이하의 경우
    elif income >= 10000 and income < 20000:
        result = str(((income-10000)*0.15)+1000)
    # 2만불초과의 경우
    elif income >= 20000:
        result = str(((income-20000)*0.2)+2500)
    # 출력 메시지 작성
    msg = "소득세는 "+ result + "달러입니다."
    # 함수 반환 값
    return msg

# 소득 금액 입력받기
print(calculate_tax(float(input("소득 금액을 입력하세요: "))))