array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)

#스와프 소스코드
#0 인덱스와 1 인덱스의 원소 교체하기
array = [3,5]
array[0], array[1] = array[1], array[0]
print(array)