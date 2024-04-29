# 사용자 나이대를 영어로 표현하는 프로그램
# 나이 입력받기
age = int(input("나이를 입력하세요: "))
# 13세에서 19세사이의 경우 "Teenager"로 분류하고 출력
if age >= 13 and age <= 19:
    print("You are in the 'Teenager' age group.")
# 20세에서 64세사이의 경우 "Adult"로 분류하고 출력
elif age >= 20 and age <= 64:
    print("You are in the 'Adult' age group.")
# 65세에서 이상의 경우 "Senior"로 분류하고 출력
elif age >= 65:
    print("You are in the 'Senior' age group.")
# 범위에 맞지 않는 경우 "Unknown age group"이라고 출력
else:
    print("You are in the 'Unknown age group' age group.")