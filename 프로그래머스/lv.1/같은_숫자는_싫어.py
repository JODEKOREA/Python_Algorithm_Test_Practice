def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

#다른 풀이
def no_continuous(s):
    a = []
    for i in s:
        #a[-1:]는 마지막 글자를 리스트로 만든 것
        if a[-1:] == [i]: continue
        a.append(i)
    return a