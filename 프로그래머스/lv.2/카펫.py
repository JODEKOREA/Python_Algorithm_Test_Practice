def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    
    for i in range(sum, 0, -1):
        if sum % i == 0:
            if (i - 2) * (sum // i - 2) == yellow:
                return [i, sum // i]
            
#다른 풀이
def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)