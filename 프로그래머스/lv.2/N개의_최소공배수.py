#유클리드 호제법(gcd, lcm)
def gcd(a, b):
    if a % b == 0:
        return b 
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    answer = arr[0]
    num = 0
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer