def solution(s):
    answer = ''
    word_list = list(map(str, s.split(" ")))
    for word in word_list:
        if word:
            word = word[0].upper() + word[1:].lower()
        answer = answer + word + " "
        
    return answer[:-1]

#이런 함수도 있네?
def Jaden_Case(s):
    return s.title()

#join() 함수 활용
def solution(s):
    answer = []
    word_list = list(map(str, s.split(" ")))
    for word in word_list:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
        
    return " ".join(answer)