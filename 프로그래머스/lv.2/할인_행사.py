def solution(want, number, discount):
    day = 0
    possible = 0
    want_list = []
    cnt = 0 
    for i in range(len(number)):
        for j in range(number[i]):
            want_list.append(want[i])
    
    while True:
        if (day + 10) == len(discount) + 1 and possible == 0:
            return 0
            break
        if (day + 10) == len(discount) + 1 and possible != 0:
            return possible
            break
        ten_discount = discount[day: day + 10]
        for x in want:
            if want_list.count(x) <= ten_discount.count(x):
                cnt += 1
        
        if cnt == len(want):
            possible += 1

#counter를 이용한 풀이
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer