import sys

n = int(input())
store_parts = list(map(int, input().split()))

m = int(input())
demanded_parts = list(map(int, input().split())) #set() 함수를 통해 집합 자료형으로 해결할 수도 있음

for demanded_part in demanded_parts:
    if demanded_part in store_parts:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')


