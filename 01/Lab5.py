# 키보드로부터 입력 받은 한글 성별을 영어로 변환하는 프로그램
# 한글 성별 입력 받기
gender = input("성별을 한글로 입력하세요 (남자/여자): ")
# "남자"를 입력한경우 "MAN"을 출력하기
if gender == "남자":
    print("MAN")
# "여자"를 입력한경우 "MOMAN"을 출력하기
elif gender == "여자":
    print("MOMAN")
# 이외의 문자를 입력한경우 대해서는오류메시지를 출력하기
else:
    print("잘못된 입력입니다.")