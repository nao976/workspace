scores = [88, 92, 75, 65, 79, 84, 91, 87, 90, 88]
# scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

center = int(len(scores)/2)
# print(center) #5
# print(scores[center]) #79

a = scores[:center]
# print(a)
print("1학기 최고 점수:",max(a))

b = scores[center:]
# print(b)
print("2학기 최고 점수:",max(b))