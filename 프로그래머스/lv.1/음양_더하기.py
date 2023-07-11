def solution(absolutes, signs):
    arr = []
    for i in range(len(signs)):
        if signs[i] is True:
            arr.append(absolutes[i])
        else:
            arr.append(absolutes[i] * (-1))
    
    return sum(arr)

#zip함수 활용
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer