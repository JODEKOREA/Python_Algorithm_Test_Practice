#그리디 알고리즘 활용. '최대' 2명씩
def solution(people, limit):
    people = sorted(people)
    min_index = 0
    max_index = len(people) - 1
    cnt = 0
    
    while min_index <= max_index:
        if people[min_index] + people[max_index] <= limit:
            cnt += 1
            min_index += 1
            max_index -= 1
        else:
            cnt += 1
            max_index -= 1
        
    return cnt