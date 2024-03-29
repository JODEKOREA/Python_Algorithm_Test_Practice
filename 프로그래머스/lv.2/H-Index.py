def solution(citations):
    answer = 0
    citations = sorted(citations, reverse = True)
    
    #H_index가 존재하고 H_index를 넘는 논문이 몇 개인지 구할 때
    for i in range(len(citations)):
        if(citations[i] < i + 1):
            return i
    
    #인용 횟수가 모두 같을 때는 전체를 return    
    return len(citations)