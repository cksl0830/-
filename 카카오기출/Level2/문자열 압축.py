def solution(s):
    if len(s) in [1,2]:
        return len(s)
    
    answer = len(s)
    n=len(s)//2
    
    for i in range(1,n+1):
        temp=s[:i]
        cnt=1
        result=''
        for j in range(i,len(s),i):
            if s[j:j+i]==temp:
                cnt+=1
            else:
                if cnt==1:
                    result+=temp
                else:
                    result+=(str(cnt)+temp)
                    cnt=1
                temp=s[j:j+i]
                
        if cnt!=1:
            result+=(str(cnt)+temp)
        else:
            result+=temp
            
        answer=min(answer,len(result))   
        
    return answer

            
