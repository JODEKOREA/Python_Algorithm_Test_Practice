def solution(nums):
    answer = len(nums) / 2 
    uniq = set(nums)
    if len(uniq) < answer:
        answer = len(uniq)
    return answer

# 한 줄 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))