def solution(cards1, cards2, goal):
    answer = 'Yes'

    cards1_index, cards2_index = 0, 0
    
    for word in goal:
        if len(cards1) > cards1_index and word == cards1[cards1_index]:
            cards1_index += 1
        elif len(cards2) > cards2_index and word == cards2[cards2_index]:
            cards2_index += 1
        else:
            answer = 'No'
            break
    
    return answer

# pop()을 활용
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"