def solution(n, m):
    answer = []
    max_num = 0
    min_num = 0
    num = 1
    if(n > m):
        for i in range(m, 0, -1):
            if (n % i == 0 and m % i == 0):
                min_num = i
                break
    else:
         for i in range(n, 0, -1):
            if (n % i == 0 and m % i == 0):
                min_num = i
                break
    while True:
        if(num % n == 0 and num % m == 0):
            max_num = num
            break
        num += 1
    
    answer = [min_num, max_num]
    
    return answer


#gcd 활용
import math

def solution(n, m):
    su1 = math.gcd(n,m)
    su2 = n * m // su1
    return su1, su2