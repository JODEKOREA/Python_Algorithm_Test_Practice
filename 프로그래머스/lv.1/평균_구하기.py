def solution(arr):
    sum = 0
    cnt = 0
    for i in arr:
        sum += i
        cnt += 1
    return sum/cnt
        