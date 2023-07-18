from itertools import combinations

def solution(nums):
    cases = []
    num_list = list(combinations(nums, 3))
    for i in num_list:
        cases.append(sum(i))
    
    cnt = 0
    for i in cases:
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check += 1
        if check == 0:
            cnt += 1
    
    return cnt

#for/else 문을 활용한 다른 풀이
from itertools import combinations

def solution(nums):
    cnt = 0
    num_list = list(combinations(nums, 3))
    for num in num_list:
        num = sum(num)
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            cnt += 1
    
    return cnt