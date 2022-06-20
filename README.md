# Python 알고리즘 코테 준비

## 1. 메소드 정리 

- #### strip()
  >양끝 공백 제거 (왼쪽은 lstrip / 오른쪽은 rstrip)

* #### rjust, ljust, zfill     [str 정렬함수]
  > 오른쪽 정렬, 왼쪽 정렬, 왼쪽부터 0으로 채움    
  > val = "77".rjust(5, "0") --> '00077'    
  > val = "22".ljust(3, "0") --> '220'    
  > val = "2".zfill(3) ---> '002'

* #### startswith 접두어 함수
  > s = '가나다라 마바사아 자차카타 파하'    
  > s.startswith('가나다')    
  > True 값 반환 


## 2. 모듈 정리
- #### from collections import Counter
  > list = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi']    
  dict = collections.Counter(list)   
  print(counter)   
  Counter({'kim': 5, 'choi': 3, 'park': 2})   
  
  > counter끼리 뺄셈도 가능하다! (마라톤 완주 문제에서 사용) 


- #### from bisect import bisect_left, bisect_right
   ```
   def calCountsByRange(nums, left_value, right_value): 
     r_i = bisect_right(nums, right_value) 
     l_i = bisect_left(nums, left_value) 
     return r_i - l_i 
     
   nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6] # 5 ~ 7 을 갖는 요소의 개수 구하기 
   nums.sort() # 정렬은 필수 
   print(calCountsByRange(nums, 5, 7)) 
   
   ''' 결과값 6 '''
   ```
   > bisect_left(a, x)    
   정렬된 a에 x를 삽입할 위치를 리턴해준다. x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.

  > bisect_right(a, x)    
  bisect_left와 거의 같은 함수인데, 이번에는 x가 a에 이미 있으면 기존 항목 뒤 (오른쪽)의 위치를 반환한다.
  
 

