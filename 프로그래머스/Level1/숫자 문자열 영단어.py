def solution(s):
    answer =''
    word=''
    dic={
        'zero':'0','one':'1','two':'2','three':'3','four':'4',
        'five':'5','six':'6','seven':'7','eight':'8','nine':'9'
        }
    for i in s:
        if i in '0123456789':
            answer+=i
        else:
            word+=i
            if word in dic.keys():
                answer+=dic[word]
                word=''

    return int(answer)
  
    
    
//다른사람의 풀이1 (for문 변수2개)
  
  num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


//다른 사람의 풀이2 (for문 변수1개)

def solution(s): 
    dic = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9} 
    for i in dic: 
        s = s.replace(i,str(dic[i])) 
        
    return int(s)


