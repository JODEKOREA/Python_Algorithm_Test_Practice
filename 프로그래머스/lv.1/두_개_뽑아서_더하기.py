from itertools import combinations

def solution(numbers):
    answer = []
    case = list(combinations(numbers, 2))
    for i in case:
        answer.append(sum(i))
    answer = sorted(list(set(answer)))
    return answer

#이중 반복문 활용
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))