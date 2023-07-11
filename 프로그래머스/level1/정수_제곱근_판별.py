def solution(n):
    num = 1
    while (n >= num):
        num2 = num ** 2
        if (n == num2):
            return (num + 1) ** 2
        elif(n < num2):
            return -1
        else:
            num += 1
            continue

# 아래와 같은 방식도 가능
def nextSqure(n):
    #1부터 입력한 숫자까지 탐색
    for x in range(1,n) :
        if x ** 2 == n :
            return (x+1) ** 2
    return "no"

# sqrt 함수를 활용할 수도 있다
def nextSqure(n):
    sqrt = n ** (1/2)
# sqrt % 1 == 0라는 것은 제곱근이 정수라는 것을 의미함
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1