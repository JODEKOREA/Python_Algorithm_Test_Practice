def solution(s):
    head = s[0]
    if head == '-':
        return -1 * int(s[1:])
    elif head == '+':
        return int(s[1:])
    else:
        return int(s)
    
#정말 쉽게 풀 수 있었던 문제. 정수형으로 바뀔 때 +, - 기호는 알아서 음, 양으로 인식한다
def strToInt(str):
    result = int(str)
    return result