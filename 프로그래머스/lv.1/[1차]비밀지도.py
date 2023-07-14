#비트 연산자 활용. &, |, ^, ~
def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        #결과값이 0bXXXX 이런 식으로 나오므로
        tmp = bin(num1 | num2)[2:]
        #tmp의 길이가 지도의 한 변 크기 보다 작다면 앞을 0으로 채워줌
        if len(tmp) < n:
            tmp = '0' * (n-len(tmp)) + tmp
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
    return answer