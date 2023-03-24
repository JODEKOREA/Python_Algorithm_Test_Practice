#설탕과자 뽑기

a,b = map(int, input().split())
num = int(input())

plate = []
for i in range(a+1):
    plate.append([])
    for j in range(b+1):
        plate[i].append(0)

for i in range(num):
    l,d,x,y = map(int, input().split())
    for j in range(l):
        if d == 0:
            plate[x][y+j] = 1
        else:
            plate[x+j][y] = 1 

for i in range(1, a+1):
    for j in range(1, b+1):
        print(plate[i][j], end= ' ')
    print()
    
