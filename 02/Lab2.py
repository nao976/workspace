import random

random_list = []

num = int(input("N값을 입력하세요 (1-100): "))
if num < 1 or num > 100:
    print("에러: N은 1 이상 100 이하의 정수여야 합니다.")
else: 
    while True:
        random_number = random.randint(1, 100)
        if random_number not in random_list:
            random_list.append(random_number)

        if len(random_list) >= num:
            break

    print("생성된 리스트: ", random_list)
    index = int(input(f"원하는 원소의 인덱스를 입력하세요 (0-{len(random_list)-1}):"))
    if index < 0 or index >= len(random_list):
        print("에러:유호한 인덱스 범위를 벗러나갔습니다.")
    else:
        print(f"선택한 인덱스의 원소: {random_list[index]}")