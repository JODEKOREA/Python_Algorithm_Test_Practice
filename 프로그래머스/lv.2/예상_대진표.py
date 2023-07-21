#수학적 규칙 발견하기
def solution(n,a,b):
    cnt = 0
    
    while a != b:
        cnt += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    
    return cnt

#다른 풀이
def solution(n, a, b):
    answer = 0
    while True:
        if a  == b:
            break
        else:
            if a % 2 == 1:
                a = a // 2 + 1
            else:
                a = a // 2
            if b % 2 == 1:
                b = b // 2 + 1
            else:
                b = b // 2
            answer += 1
    return answer