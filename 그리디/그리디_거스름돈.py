n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    count += n // coin
    n %= coin

print(count)