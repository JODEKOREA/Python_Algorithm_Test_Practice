def solution(arr, divisor):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            new_arr.append(arr[i])
    if len(new_arr) == 0:
        return [-1]
    else:
        return sorted(new_arr)
    
# 리스트 컴프리헨션 활용

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]