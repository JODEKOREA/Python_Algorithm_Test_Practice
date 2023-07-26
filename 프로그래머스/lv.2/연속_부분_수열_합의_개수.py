def solution(elements):
    sum_list = []
    elements_len = len(elements)
    elements = 2 * elements
    
    for i in range(elements_len):
        for j in range(elements_len):
            sum_list.append(sum(elements[j: j + i + 1]))    
    
    return len(set(sum_list)) 