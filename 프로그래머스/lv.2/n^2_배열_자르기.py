#내 틀린 풀이. 시간복잡도에서 문제 발생. 규칙 발견 필요
def solution(n, left, right):
    arrays = []
    new_array = []
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            arrays[i][j] = max(i, j) + 1
    
    for array in arrays:
        new_array += array

    return new_array[left:right+1]

#몫과 나머지로 접근. 형렬은 몫과 나머지로 접근할 수 있다!
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n 
        answer.append(max(a,b) + 1)
        
    return answer

#divmod()함수를 활용
def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        q, r = divmod(i, n)

        answer.append(max(q, r) + 1)

    return answer