def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if (i ** (1/2)) % 1 == 0:
            result -= i
        else:
            result += i
    return result

#약수를 구하는 함수를 활용하는 예시
def find_divisor(num):
   count = 0
   for i in range(1, num+1):
      if num%i==0:
            count += 1
    # 짝수이면 1
   if count%2 == 0:
      return 1
   # 홀수이면 0
   else:
      return 0
def solution(left, right):
   ans = 0
   for i in range(left,right+1):
      if find_divisor(i) == 0:
         ans-=i
      else: 
         ans+=i
   return ans