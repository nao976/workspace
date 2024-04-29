# 영어 방향 명령어 해석하는 프로그램
# "left", "right", "up", "down" 중 하나의 단어를 입력받기
direction = input("방향을 입력하세요(left, right, up, down): ")
# 입력받은 방향에 따른 메시지를 출력하기
if direction == "left":
    print("왼쪽으로 이동합니다.")
elif direction == "right":
    print("오른쪽으로 이동합니다.")
elif direction == "up":
    print("위로 이동합니다.")
elif direction == "down":
    print("아래로 이동합니다.")
else:
    print("알 수 없는 명령입니다.")