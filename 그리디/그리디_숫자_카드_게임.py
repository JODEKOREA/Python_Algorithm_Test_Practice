n, m = map(int, input().split())
array = []
min_num = 0

for i in range(n):
    array.append([])
    s = list(map(int, input().split()))
    for j in range(m):
        array[i].append(s[j])

for i in range(1,n):
    min_num = min(array[0])
    if min(array[i]) > min_num:
        min_num = min(array[i])

print(min_num)