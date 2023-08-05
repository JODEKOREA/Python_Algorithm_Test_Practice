#deque을 활용한 풀이

from collections import deque

def solution(cacheSize, cities):
    stack = deque(maxlen = cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            time = len(cities) * 5
        else:
            if city not in stack:
                stack.append(city)
                time += 5
            else:
                stack.remove(city)
                stack.append(city)
                time += 1
          
    answer = time
    return answer

#다른 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time