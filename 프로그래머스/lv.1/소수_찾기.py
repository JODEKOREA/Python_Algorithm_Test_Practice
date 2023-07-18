def solution(n):
    num = [False, False] + [True] * (n - 1)
    prime_num = []
    
    for i in range(2, n + 1):
        if num[i]:
            prime_num.append(i)
        for j in range(2 * i, n + 1, i):
                num[j] = False
        
    return len(prime_num)


#에라토스테네스의 체를 구현한 다른 간단한 풀이
def solution(n):
    num=set(range(2,n+1))
    print(num)

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    print(len(num))
