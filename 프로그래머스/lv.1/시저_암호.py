def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
        elif (ord(s[i].lower())) + n > ord('z'):
            answer += chr(ord(s[i]) - 26 + n)
        else:
            answer += chr(ord(s[i])+n)
    return answer

#더 깔끔한 풀이. isupper()와 islower() 사용
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)