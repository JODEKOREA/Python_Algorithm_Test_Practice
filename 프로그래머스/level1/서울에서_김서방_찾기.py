def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"
        
# 인덱스 함수 활용
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))