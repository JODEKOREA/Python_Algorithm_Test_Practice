def solution(sizes):
    answer = 0
    num_list1 = []
    num_list2 = []
    for i in range(len(sizes)):
        sizes[i].sort()
    for i in range(len(sizes)):
        num_list1.append(sizes[i][0])
        num_list2.append(sizes[i][1])
    
    return max(num_list1) * max(num_list2)

#더 간단한 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes) 