def solution(s):
    num_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cnt = 0
    for i in range(len(s)):
        if s[i] in num_set:
            cnt += 1
    if (cnt == 4 and len(s) == 4) or (cnt == 6 and len(s) == 6):
        return True
    else:
        return False

#isdigit()을 이용한 풀이. isalpha()라는 함수도 존재
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]