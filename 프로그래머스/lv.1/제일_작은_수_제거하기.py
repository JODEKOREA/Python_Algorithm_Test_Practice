def solution(arr):
    if len(arr) == 1:
        arr = [-1]
    else:
        min_num = min(arr)
        arr = [num for num in arr if num != min_num]
    return arr