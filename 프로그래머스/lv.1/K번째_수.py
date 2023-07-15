def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        num_list = sorted(array[commands[i][0] - 1: commands[i][1]])
        num = num_list[commands[i][2] - 1]
        answer.append(num)
    return answer

#좀 더 단순한 풀이
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

#리스트 컴프리헨션 사용
def solution(array, commands):
    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]