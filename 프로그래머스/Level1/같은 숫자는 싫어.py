def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer
  
  
// 다른 사람의 풀이1  (풀이1,2 둘다 슬라이싱 활용!)  #  [-1] --> 빈배열이어도 에러 안나는거 잊지말자!

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
  
  
// 다른 사람의 풀이2

def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result
