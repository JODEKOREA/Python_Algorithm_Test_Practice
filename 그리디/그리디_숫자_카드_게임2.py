n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    #가장 작은 수들 중 가장 큰 수 찾기

print(result)