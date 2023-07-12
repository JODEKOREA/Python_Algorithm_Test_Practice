#이중 반복문을 통한 행렬의 덧셈 구현

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

#zip()함수를 통한 구현
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer