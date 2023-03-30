from collections import deque, Counter

#deque 활용
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
#리스트 자료형으로 변환
print(list(data))

#Counter 활용

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
