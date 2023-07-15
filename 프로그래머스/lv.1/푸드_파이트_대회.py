#리스트 슬라이싱 활용법

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2) 
    return answer + '0' + answer[::-1]