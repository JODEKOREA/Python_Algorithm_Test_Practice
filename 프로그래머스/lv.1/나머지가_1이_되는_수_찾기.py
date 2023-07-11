def solution(n):
    x = 0
    for i in range(n-1, 0, -1):
        if n % i == 1:
            x = i
    return x
