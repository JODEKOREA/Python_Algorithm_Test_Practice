#몫과 나머지를 반환해주는 divmod(x, y) 함수. n진법으로 전환해주는 int(x, n)함수
def solution(n):
    answer = ''
    result = 0
    
    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)
    
    result = int(answer, 3)
    
    print(result)

# 다른 풀이
def solution(n):
    tmp = ''
    #while 0이 False라는 점을 활용 
    while n:
        tmp += str(n % 3)
        #몫을 반환
        n = n // 3

    answer = int(tmp, 3)
    return answer