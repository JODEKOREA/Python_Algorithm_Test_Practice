def solution(answers):
    answer = []
    prob1 = [1, 2, 3, 4, 5]
    prob2 = [2, 1, 2, 3, 2, 4, 2, 5]
    prob3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if prob1[i % 5] == answers[i]:
            score[0] += 1
        if prob2[i % 8] == answers[i]:
            score[1] += 1
        if prob3[i % 10] == answers[i]:
            score[2] += 1
            
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    
    return answer

#enumerate 사용
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result