from collections import defaultdict 

def solution(fees, records):
    answer = []
    dic=defaultdict(list)
    
    for record in records:
        record=record.split()
        temp=record[0].split(':')
        dic[record[1]].append(temp)
        
    dic=dict(sorted(dic.items()))
    
    for v in dic.values():
        time=0
        price=0
        
        for t in range(len(v)//2):
                time+= ((int(v[(2*t)+1][0])-int(v[2*t][0]))*60) #시
                time+= (int(v[(2*t)+1][1])-int(v[2*t][1])) #분 
        #입차까지만 되고 출차는 밤에 되는 경우
        if len(v)%2:
            time+= ((23-int(v[-1][0]))*60)
            time+= (59- int(v[-1][1]))
            
        if time<=fees[0]:
                price=fees[1]
        elif (time-fees[0]) % fees[2]:
            price = fees[1] + ((time-fees[0])//fees[2]+1)*fees[3]
        else:
            price = fees[1] + ((time-fees[0])//fees[2])*fees[3]
            
        answer.append(price)
        
    return answer
