def solution(n):
    result = []
    final_str = ''
    new = list(str(n))
    new = sorted(new, reverse = True)
    for i in range(len(new)):
        result.append(new[i])
    for i in range(len(result)):
        final_str += result[i]
    return int(final_str)

#join 함수를 활용한 간단한 풀이
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))