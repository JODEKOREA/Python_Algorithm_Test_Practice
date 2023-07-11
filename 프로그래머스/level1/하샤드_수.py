def solution(x):
    div = 0
    original_num = x
    while(x > 10):
        div += x % 10
        x //= 10
    div += x
    if(original_num % div == 0):
        return True
    else:
        return False
        
#str을 활용한 풀이
def Harshad(n):
    return n % sum(int(x) for x in str(n)) == 0