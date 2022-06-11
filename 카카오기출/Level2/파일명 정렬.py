def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''

        flag = True
        
        for i in range(len(file)): 
            if file[i].isdigit():  
                number += file[i]
                flag = False
            elif flag:  
                head += file[i]
            else:               
                tail = file[i:]
                break
                
        answer.append((head, number, tail)) 

    answer.sort(key=lambda x: (x[0].lower(), int(x[1]))) 

    return [''.join(s) for s in answer]
