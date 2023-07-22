def solution(n):
    #1만큼은 무조건 건전지를 사용해야 한다
    energy = 1
    
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            energy += 1

    return energy