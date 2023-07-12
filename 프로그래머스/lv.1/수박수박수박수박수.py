def solution(n):
    str= ''
    for i in range(n):
        if i % 2 == 0:
            str += '수'
        else:
            str += '박'
    return str

#참신하고 간단한 풀이
def water_melon(n):
    str = "수박"*n
    return str[:n]