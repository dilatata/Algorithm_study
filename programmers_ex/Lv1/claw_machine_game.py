'''
크레인 인형뽑기 게임

[제한사항]
board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
0은 빈 칸을 나타냅니다.
1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
moves 배열의 크기는 1 이상 1,000 이하입니다.
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
'''
# 입출력 예
'''
board
[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]]

moves
[1,5,3,5,1,2,1,4]

result
4
'''
# logic 생각하기
'''
moves의 값 m 
1. board[i][m] 으로 가장 작은 i 값 대입해서 0이 아닌 수 나오는 인덱스값 찾기
2. 해당 값 리스트에 넣고 board에서 0으로 변경하기

만들어진 리스트에서 인접값이 같은 경우의 수 찾기
'''
board = [[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# print(board[2][1])
def solution(board, moves):
    doll = []
    answer = 0

    for move in moves:
        for i in range(len(board)): 
            if board[i][move-1] != 0:
                doll.append(board[i][move-1])
                board[i][move-1] = 0
                break
            else:
                continue
    # print(doll)

    for a in range(len(doll)):
        for i in range(1,len(doll)):
            if doll[i] == doll[i-1]:
                    answer += 2
                    del doll[i]
                    del doll[i-1]
                    break
    return answer
# print(solution(board, moves))

#다른 풀이 
def solution_a(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0
# if문을 사용해서 for 사용 줄이기
# stacklist 에 2개 이상 쌓이면 가장 마지막에 넣은 2개의 중복을 체크
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        # pop 사용 대신
                        # stacklist[-2:]=[] 사용도 가능
                        answer += 2     
                break

    return answer