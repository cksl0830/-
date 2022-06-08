from collections import Counter

def solution(str1, str2):
    
    arr1=[]
    arr2=[]
    
    for i in range(len(str1)-1):
        temp=""
        temp+=str1[i:i+2]
        if temp.isalpha():
            temp=temp.lower()
            arr1.append(temp)
    
    for i in range(len(str2)-1):
        temp=""
        temp+=str2[i:i+2]
        if temp.isalpha():
            temp=temp.lower()
            arr2.append(temp)
            
    counter1=Counter(arr1)
    counter2=Counter(arr2)
    
    # elements()가 요소들 다 꺼내기 때문에 자카드 유사도의 중복허용 가능
    inter = list((counter1 & counter2).elements())  
    union = list((counter1 | counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
