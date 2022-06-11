maxScore = 0		# 가장 큰 점수 차이
maxList = []		# 가장 큰 점수 차이를 낸 배열 
ryan = [0]*11       # 라이언 스코어

def solution(n, info):
    
    ryanScore(0, n, info)		
    
    if not maxList: 
        return [-1]
    else: 
        return maxList


def ryanScore(i, n, apeach) :	
    
    if n == 0 : 				
        calScore(ryan, apeach)
        return
    
    if i == 11: 
        return	
    
    apeachScore = apeach[i]			
    cnt=apeachScore+1
    for k in range(cnt,-1,-1):
        if n >= k:
            ryan[i] = k
            ryanScore(i+1, n-k, apeach)
            ryan[i] = 0    
               
# 점수 계산 함수    
def calScore(ryan, apeach):		
    global maxScore, maxList
    rScore = 0	# 라이언 점수
    aScore = 0	# 어피치 점수
    
    for i in range(11):
        if ryan[i] == 0 and apeach[i] == 0: 
            continue	
        if ryan[i] > apeach[i] : 
            rScore += (10-i)
        else : 
            aScore += (10-i)				
            
    if rScore > aScore :		
        dif = rScore - aScore
        if dif > maxScore:		
            maxScore = dif
            maxList = ryan[:]
            
        elif dif == maxScore:			
            for i in range(10,-1,-1):	
                if ryan[i]==maxList[i]:
                    continue
                if ryan[i] > maxList[i]:
                    maxList = ryan[:]
                    break
                else:
                    break
