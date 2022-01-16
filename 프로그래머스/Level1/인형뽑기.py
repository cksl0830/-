def solution(board, moves):
    basket = []  # 인형들을 담아줄 바구니
    answer = 0  # 터진 인형들

    for move in moves:  # 사용자의 움직임 하나씩 출력
        for column in board:  # columns 출력
            # move는 1부터 시작하기 때문에 index로 사용하기 위해선 -1씩 해줘야 함
            if column[move - 1] != 0:  # 만약 column의 move가 0이 아니라면 (인형이 있다는 말)
                basket.append(column[move - 1])  # 해당 값을 인형 바구니에 담기

                if len(basket) > 1:  # 바구니에 인형이 2개 이상 들어가는데
                    if basket[-2] == basket[-1]:  # 인형이 두개가 겹친다면
                        del basket[-2]  # 터뜨린다
                        del basket[-1]  # 터뜨린다
                        answer += 2  # 터뜨린 인형 갯수 추가

                column[move - 1] = 0  # 뽑은 인형은 0 처리
                break
    return answer
    
    
// 다른 사람의 풀이 
    
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

