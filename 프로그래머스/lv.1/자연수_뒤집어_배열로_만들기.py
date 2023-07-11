def solution(n):
    answer = []
    new = str(n)
    for i in range(len(new)):
        answer.insert(0, int(new[i]))
    
    return answer

# reverse를 활용할 수도 있다!
def digit_reverse(n):
    # 함수를 완성해 주세요
    m = list(str(n))
    m.reverse()
    return [int (i) for i in m]