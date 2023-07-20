def solution(n):
    num = n + 1
    while True:
        if bin(num)[2:].count('1') == bin(n)[2:].count('1'):
            return num
        num += 1