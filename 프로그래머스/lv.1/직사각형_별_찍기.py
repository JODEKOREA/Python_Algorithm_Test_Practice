a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end ='')
    print()

#직사각형이라는 점을 활용한 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)