#문자열에서 rindex() 함수 기억하자!
def solution(s):
    answer = []
    word = ''
    for i in range(len(s)):
        if s[i] not in word:
            answer.append(-1)
            word += s[i]
        else:
            answer.append(i - word.rindex(s[i]))
            word += s[i]
    return answer

#딕셔너리를 활용한 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
