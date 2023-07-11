def solution(numbers):
    numbers = set(numbers)
    num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    no_num = num - numbers
    return sum(no_num)

#훨씬 단순한 풀이
def solution(numbers):
    return 45 - sum(numbers)