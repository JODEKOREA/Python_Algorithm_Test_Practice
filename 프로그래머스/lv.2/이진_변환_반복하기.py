#count() 함수 기억하기
def solution(s):
    x = ''
    cnt = 0
    removed_zero = 0
    while True:
        cnt += 1 
        x = s.count('1') * '1'
        removed_zero += len(s) - len(x) 
        s = bin(len(x))[2:]
        if len(s) == 1:
            break
        
    
    return [cnt, removed_zero]