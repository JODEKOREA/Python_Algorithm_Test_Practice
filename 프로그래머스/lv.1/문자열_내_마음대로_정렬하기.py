# 약간의 창의력
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
            
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    
    return answer

# 람다를 활용한 풀이
def solution(strings, n):
    #해당 문제에서는 한 번의 정렬이 더 필요함
    return sorted(sorted(strings), key = lambda x: x[n])

# 새로운 함수 생성
def solution(strings, n):
    def sortkey(x):
        return x[n]
    #사전순으로 정렬
    strings = sorted(strings)
    #n번째 글자 기준으로 정렬
    strings.sort(key = lambda x: sortkey(x))
    return strings