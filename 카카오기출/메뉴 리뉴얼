from itertools import combinations
from collections import defaultdict

def solution(orders, course):

    temp = defaultdict(list)

    for order in orders:
        for num in course:
            if num > len(order):
                break
            else:
                temp[num] += list(combinations(sorted(list(order)),num))

    result = set()
    for menus in temp.values():
        max_num = 2
        for menu in menus:
            cnt = menus.count(menu)
            if cnt>max_num:
                max_num = cnt

        for menu in menus:
            if max_num == menus.count(menu):
                m = ''.join(menu)
                result.add(m)
                
    return sorted(result)
 
 
 // 다른 풀이 

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for s in orders:
            arr = combinations(sorted(s), i)
            temp += arr
        count = Counter(temp)
        
        
        if count:  #한개만 있을 때를 대비하여 max값 위해 체크해줘야함 
            if max(count.values()) >= 2:
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)
    
    
