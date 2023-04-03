#나이트 위치 입력받기
input_data = input()
row = int(input_data[1])
#알파벳을 숫자로 변환하여 연산
column = int(ord(input_data[0]))-int(ord('a')) + 1

count = 0

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#각 위치로 이동이 가능한지 확인
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)
