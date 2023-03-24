num = int(input())
called_name = input().split()

for i in range(num):
    called_name[i] = int(called_name[i])
    
name = []
for i in range(24):
    name.append(0)

for i in range(num):
    name[called_name[i]] += 1 

for i in range(1, 24):
    print(name[i], end = ' ')
