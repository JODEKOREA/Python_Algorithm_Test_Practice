def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    
    for value in closet.values():
        answer *= len(value) + 1
    #하나는 반드시 선택해야 하므로 
    return answer - 1

#해시를 활용한 정석적인 풀이
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            #아무것도 안 입는 경우까지 고려
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1