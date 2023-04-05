n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))    

result = sorted(num_list, reverse = True)

for num in result:
    print(num, end = ' ')