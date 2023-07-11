def solution(n):
    sum = 0
    while True:
        sum += n % 10
        n //= 10
        if(n == 10):
            sum += 1
            n = 0
            break
        elif(n < 10):
            break
    sum += n
    return sum

#문자열을 사용하는 풀이도 있더라!

def solution(n):
    new = str(n)
    add = 0
    for i in range(len(new)):
        add += int(new[i])
    return add

#재귀함수로 구현할 수도 있다!

def sum_digit(number):
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)