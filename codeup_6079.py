a = int(input())
sum = 0

for i in range(50):
    sum = sum + i
    
    if (sum >= a):
        print(i)
        break
