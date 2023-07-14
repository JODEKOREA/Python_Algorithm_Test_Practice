#딕셔너리를 활용한 풀이
def solution(s):
    num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
'eight': 8, 'nine': 9, 'zero': 0}
    for key, value in num.items():
        s = s.replace(key, str(value))
    
    return int(s)

#리스트를 활용한 풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)