n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    #현재 줄에서 최소 값 찾기
    for a in data:
        min_value = min(min_value, a)
    #가장 작은 수들 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
