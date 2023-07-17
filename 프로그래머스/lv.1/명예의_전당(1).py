def solution(k, score):
    answer = []
    honor = []
    for i in range(len(score)):
        if len(honor) < k:
            honor.append(score[i])
            answer.append(min(honor))
        else:
            honor.append(score[i])
            honor = sorted(honor, reverse = True)
            answer.append(honor[k-1])
    return answer

# 다른 풀이
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer