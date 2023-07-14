#sorted()와 sort() 활용법
def solution(d, budget):
    d = sorted(d)
    cnt = 0
    for i in range(len(d)):
        if budget >= d[i]:
            cnt += 1
            budget -= d[i]
        else:
            break
        
    return cnt