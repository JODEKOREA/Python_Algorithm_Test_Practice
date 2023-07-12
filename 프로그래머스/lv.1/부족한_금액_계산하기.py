def solution(price, money, count):
    total_price = 0
    for i in range(count):
        total_price += price * (i + 1)
    
    if money - total_price < 0:
        return total_price - money
    else:
        return 0
    
#max를 활용한 연산
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)