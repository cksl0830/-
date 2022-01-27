def solution(s):
    answer1 = []
    answer2 = []
    for words in s:
        if words.islower():
            answer1.append(words)

    for words in s:
        if words.isupper():
            answer2.append(words)

    answer1.sort(reverse=True)
    answer2.sort(reverse=True)
    return "".join(answer1+answer2)
  
  
// 다른 사람의 풀이 ( ..? )

def solution(s):
    return ''.join(sorted(s, reverse=True))
