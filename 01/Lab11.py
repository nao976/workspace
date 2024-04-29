# 섭씨 온도를 화씨 온도로 변환하고 출력하는 프로그램
# 온도 변환 함수
def convert_celsius_to_fahrenheit(celsius):
    # 화씨 온도 계산하기
    result = str(celsius*9/5+32)
    # 출력 메시지 작성
    msg = "화씨 온도는 " + result + "입니다."
    # 함수 반환 값
    return msg

# 섭씨 온도 입력받기
print(convert_celsius_to_fahrenheit(int(input("섭씨 온도를 입력하세요: "))))
