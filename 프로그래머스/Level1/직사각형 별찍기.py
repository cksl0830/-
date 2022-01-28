a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*'*a)
    
// 다른 사람 풀이

print(('*'*a +'\n')*b)
