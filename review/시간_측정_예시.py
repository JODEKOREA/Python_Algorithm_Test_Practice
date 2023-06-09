#선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

#선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print("선택 정렬 성능 측정:", end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

#기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)
