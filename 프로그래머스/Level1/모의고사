def solution(answers):
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 

    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]: count1 += 1
        if answers[i] == s2[i % len(s2)]: count2 += 1
        if answers[i] == s3[i % len(s3)]: count3 += 1

    mac = max(count1, count2, count3) 

    if (mac == count1): answer.append(1)
    if (mac == count2): answer.append(2)
    if (mac == count3): answer.append(3)

    return answer
    
 // 다른 사람의 풀이 (enumerate 사용 ,,)
 
 def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
