from itertools import permutations, product, combinations, combinations_with_replacement

#모든 순열 구하기 (중복 허용 X)
data = ['A','B','C']
result = list(permutations(data))
print(result)

#모든 순열 구하기 (중복 허용 O)
result = list(product(data, repeat = 2))
print(result)

#2개를 뽑는 모든 조합 구하기(중복 허용 X)
result = list(combinations(data, 2))
print(result)

#2개를 뽑는 모든 조합 구하기(중복 허용 O)
result = list(combinations_with_replacement(data, 2))
print(result)