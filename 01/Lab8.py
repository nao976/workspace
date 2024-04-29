# 하나의 영문자를 입력받고 모음인지 판별하고 결과를 출력하는 프로그램
# 하나의 문자 입력빋기
inputStr = input("한 문자를 입력하세요: ")
# 입력받은 문자가 모음인 경우
if inputStr == "a" or inputStr == "e" or inputStr == "i" or inputStr == "o" or inputStr == "u":
    print(inputStr+"는 모음입니다.")
# 모음이 아닌 경우
else:
    print(inputStr+"는 모음이 아닙니다.")