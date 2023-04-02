n = int(input())
map = []
x = 1
y = 1

direction = input().split()
for move in direction:
    if move == 'R':
        if y == 5:
            continue
        else:
            y += 1
    elif move == 'L': 
        if y == 1:
            continue
        else:
            y -= 1
    elif move == 'U':
        if x == 1:
            continue
        else:
            x -= 1
    else:
        if x == 5:
            continue
        else:
            x += 1

print(x, y)    
