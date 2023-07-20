def solution(A,B):
    answer = 0
    
    A1 = sorted(A)
    B1 = sorted(B, reverse = True)
    for x,y in zip(A1, B1):
        answer += x*y
        
    return answer

#짧은 코드
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])