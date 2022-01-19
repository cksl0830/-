# Python 알고리즘 코테 준비


## 1. 메소드 정리 
- #### lower()
  >대문자를 소문자로 변환하는 문자열 메소드 

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

- #### zip() & enumerate()
  > 여러 자료형 묶을 때 사용 (동일한 개수)

- #### 1.map(함수,입력(리스트))    
  #### 2.lambda(매개변수:표현식) 
  > map(lamda, 인자) :: 이런식으로 묶어서 많이 사용


## 2. 모듈 정리
- #### collections 모듈의 counter
  > list = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi']    
  dict = collections.Counter(list)   
  print(counter)   
  Counter({'kim': 5, 'choi': 3, 'park': 2})   
  
  > counter끼리 뺄셈도 가능하다! (마라톤 완주 문제에서 사용) 
