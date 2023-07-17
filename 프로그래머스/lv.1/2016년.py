def solution(a, b):        
    answer = ''
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = day[(sum(days[0:a]) + b - 1) % 7 ]
    return answer