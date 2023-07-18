def solution(s):
    num_list = s.split(' ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
        
    return ""+ str(min(num_list)) + " " + str(max(num_list))

#다른 풀이
def solution(s):
    num_list = list(map(int, s.split()))
    return str(min(num_list)) + " " + str(max(num_list))