def solution(t, p):
    num = 0
    cnt = 0
    for i in range(len(t)-(len(p)-1)):
        num = int(t[i:i+len(p)])
        if(num <= int(p)):
            cnt += 1
        
    return cnt