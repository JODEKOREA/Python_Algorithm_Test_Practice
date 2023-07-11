def solution(a, b):
    num = []
    sum = 0
    if a <= b:
        for i in range(b-a + 1):
            num.append(a)
            a += 1
    else:
        for i in range(a-b + 1):
            num.append(b)
            b += 1
            
    for i in range(len(num)):
        sum += num[i]
    
    return sum

#sum 함수를 활용한 방법
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

#절대값을 이용한 방법
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

#min, max를 활용한 방법
def adder(a, b):
    return sum(range(min(a, b), max(a, b)+1))