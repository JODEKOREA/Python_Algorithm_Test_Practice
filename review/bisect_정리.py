from bisect import bisect_left, bisect_right

#bisect를 활용한 인덱스 값
a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

#bisect를 활용한 범위 안의 원소의 개수 구하기
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))