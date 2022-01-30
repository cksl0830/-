def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:] #비트 계산과 ob빼고 출력
        ans.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#").replace("0", " "))  #앞에 0마저 붙여주고 문자 대체하기 
    
    return ans


// 다른 사람의 풀이 (rjust 처음 앎 .. 굳)

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')     #  a12=a12.zfill(n) 도 가능!
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
