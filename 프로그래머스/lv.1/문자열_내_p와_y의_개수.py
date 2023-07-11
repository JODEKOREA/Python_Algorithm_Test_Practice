def solution(s):
    s = s.lower()
    p_num = 0
    y_num = 0
    for i in range(len(s)):
        #문자열를 리스트처럼 활용. 인덱스 활용
        if s[i] == 'p':
            p_num += 1
        elif s[i] == 'y':
            y_num += 1
    if p_num == y_num:
        return True
    else:
        return False
    

#훨씬 간단한 풀이

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

print( numPY("pPoooyY") )
print( numPY("Pyy") )