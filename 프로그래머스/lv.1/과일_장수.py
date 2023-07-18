def solution(k, m, score):
    answer = 0
    part = []
    score = sorted(score, reverse = True)
    for i in range(0, len(score)-(len(score)% m), m):
        answer += min(score[i:i + m]) * m
        
    return answer

#다른 풀이
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m:
            answer += min(apple) * m

    return answer