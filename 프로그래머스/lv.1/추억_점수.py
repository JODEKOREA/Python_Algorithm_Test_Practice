def solution(name, yearning, photo):
    answer = []
    score = 0
    dic = dict()
    for i in range(len(name)):
        dic[name[i]] = yearning[i] 
    
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                score += dic[photo[i][j]]
        answer.append(score)
        score = 0
    return answer

#zip 활용
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores