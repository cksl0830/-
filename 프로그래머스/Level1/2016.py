def solution(a, b):

    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]

    return day[(sum(mon[:a-1]) + b) % 7]


// 다른 사람의 풀이 (datetime 이라는 함수 활용)

import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]
