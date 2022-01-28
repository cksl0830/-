def solution(s, n):
    answer = ''
    low="abcdefghijklmnopqrstuvwxyz"*2 
    up=low.upper()


    for i in range(len(s)):
        if s[i] in low:
            answer+=low[low.index(s[i])+n]
        elif s[i] in up:
            answer+=up[up.index(s[i])+n]
        else:
            answer+=s[i]

    return answer

  
  
  // 다른 사람의 풀이 (문자를 *2 할게 아니라 나머지를 이용했어야 더 깔끔한 풀이!!)
  
  def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)
