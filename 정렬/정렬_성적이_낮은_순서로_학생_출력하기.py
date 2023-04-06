n = int(input())
students = []

#n명의 학생 정보를 입력받아 리스트에 저장
for i in range(n):
    input_list = input().split()
    students.append((input_list[0], input_list[1]))

#key값을 이용하여 점수를 기준으로 정렬
array = sorted(students, key = lambda x: x[1])

#정렬이 수행된 결과 출력
for student in students:
    print(student[0], end = ' ')