def solution(lottos, win_nums):
    answer = []
    count = 7

    # 지워진 숫자(0)가 모두 맞을 경우(최고 순위)
    for i in lottos:
        if i == 0:
            count -= 1
        elif i in win_nums:
            count -= 1
    if count > 6:
        answer.append(6)
    else:
        answer.append(count)
    count = 7

    # 지워진 숫자가 모두 틀릴 경우(최저 순위)
    for j in lottos:
        if j in win_nums: count -= 1
    if count > 6:
        answer.append(6)
    else:
        answer.append(count)

    return answer




/// 다른 사람의 풀이1

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

/// 다른 사람의 풀이2

def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
