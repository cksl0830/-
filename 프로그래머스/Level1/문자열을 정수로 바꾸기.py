def solution(s):

    return int(s)


// 다른 사람의 풀이 (알고리즘 공부차 이렇게 푸는게 정답인거 같아서 남겨둔다 .. 
 
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result
