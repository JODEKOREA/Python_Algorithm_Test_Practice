#zip()을 활용한 내 풀이
def solution(a, b):
    result = 0
    for num1, num2 in zip(a,b):
        result += num1 * num2
    return result

#한 줄 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

#람다 활용
solution = lambda x, y: sum(a*b for a, b in zip(x, y))