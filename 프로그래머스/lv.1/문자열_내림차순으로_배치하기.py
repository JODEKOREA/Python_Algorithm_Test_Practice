#sort() 함수. lambda 활용 방법 익숙해지기

def solution(s):
    small = []
    big = []
    total = []
    answer = ''
    for i in range(len(s)):
        if ord(s[i]) >= 97:
            small.append(s[i])
        else:
            big.append(s[i])
    
    small.sort(key = lambda x: ord(x), reverse = True)
    big.sort(key = lambda x: ord(x), reverse = True)
    
    total = small + big
    
    for i in range(len(total)):
        answer += total[i]
    
    return answer

#join함수 사용 

def solution(s):
    return ''.join(sorted(s, reverse=True))