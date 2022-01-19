def solution(n, lost, reserve):

    res=set(reserve)-set(lost)        # 중복번호 제거 
    los=set(lost)-set(reserve)

    for i in res:
        if i-1 in los:
            los.remove(i-1)          # 왼쪽부터 리스트 제거
        elif i+1 in los:
            los.remove(i+1)

    return n - len(los)
  
  
