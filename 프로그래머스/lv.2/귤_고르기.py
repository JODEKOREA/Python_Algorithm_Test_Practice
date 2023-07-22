def solution(k, tangerine):
    cnt = 0
    dic = {}
    for size in tangerine:
        if size in dic:
            dic[size] += 1
        else:
            dic[size] = 1
    
    #sorted()함수를 사용하게 되면 튜플로 이루어진 리스트가 생성되므로 dict()로 감싸줘야 아래 반복문을 수행할 수 있다.
    dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
    
    for i in dic:
        if k <= 0:
            return cnt
        k -= dic[i]
        cnt += 1

    return cnt

#Counter 함수 활용법

import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])