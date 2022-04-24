# Python 알고리즘 코테 준비


## 1. 메소드 정리 

- #### isalnum()
  >문자열에서 알파벳과 숫자로만 구성되었는지 확인하는 문자열 메소드

- #### isalpha()
  > 문자열이 영어 혹은 한글인지 확인

- #### isdigit()
  > 숫자로만 구성되있는지 확인 

- #### strip()
  >양끝 공백 제거 (왼쪽은 lstrip / 오른쪽은 rstrip)

- #### replace()
  > 문자대체 :: (old,new,[count])

* #### return sorted(fail, key=lambda x: fail[x], reverse=True)    # 실패율 문제 
  > 딕셔너리에서 sorted를 사용하면 key를 기준으로 정렬하는데 람다 함수를 사용해서     
  > fail[x] 즉, value를 기준으로 정렬

* #### int('n',3) 문자열 숫자 n을 3진수에서 10진수로
* #### int('n',5) 문자열 숫자 n을 5진수에서 10진수로

* #### import math ----> gcd(n,m) & lcm(n,m)   :: gdc: n,m의 최대공약수 , lcm은 최소공배수         
       최대 공약수와 최소공배수의 곱은 n * m 과 같다! 

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
- #### collections 모듈의 counter
  > list = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi']    
  dict = collections.Counter(list)   
  print(counter)   
  Counter({'kim': 5, 'choi': 3, 'park': 2})   
  
  > counter끼리 뺄셈도 가능하다! (마라톤 완주 문제에서 사용) 

- #### itertools 의 순열과 조합
  > chars = ['A', 'B', 'C']   
    p = itertools.permutations(chars, 2)  # 순열   
    c = itertools.combinations(chars, 2)  # 조합   
    p= [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]   
    c= [('A', 'B'), ('A', 'C'), ('B', 'C')]   

- #### import functools   (프로그래머스 정렬)
  ```
  def comparator(a,b):    
    t1 = a+b    
    t2 = b+a      
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) # 크면1 같으면0 작으면-1  
  ```    
    ex) functools.cmp_to_key(comparator) 

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
  


