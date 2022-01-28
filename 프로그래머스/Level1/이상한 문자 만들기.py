def solution(s):

    answer=[]
    s=s.split(" ")

    for i in range(len(s)):
        temp=""
        for k in range(len(s[i])):
            if k%2==0:
                temp+=s[i][k].upper()
            else:
                temp+=s[i][k].lower()
        answer.append(temp)

    return " ".join(answer)


