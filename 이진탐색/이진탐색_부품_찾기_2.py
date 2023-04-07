def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
store_parts = list(map(int, input().split()))
store_parts.sort() #이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())
demanded_parts = list(map(int, input().split()))

for i in demanded_parts:
    result = binary_search(store_parts, i, 0, n-1)
    if result != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')