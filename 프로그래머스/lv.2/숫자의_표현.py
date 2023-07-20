def solution(n):
    cnt = 0
    value = 0
    k = 1
    while True:
        if k == n + 1:
            break
        for i in range(k, n + 1):
            value += k
            if value == n:
                cnt += 1
            elif value > n:
                value = 0
                break
        k += 1
            
    return cnt 