# 깊이우선 탐색
# 너비우선탐색

'''
깊이우선탐색 DFS
하나의 경우의 수에 대해서 모든 경우의 수를 조사하고 다음 경우의 수를 조사하면서 해를 찾는 과정
하나의 트리구조 -> 하나의 길의 끝까지 확인 후 다른 길 조사

미로찾기
탈출 가능 true
탈출 불가능 false

이동 가능한 길 0
이동 불가능한 길 1
'''


while len(stack)>0:
    now = stack.pop()
    if now == dest:
        return True
    x = now[1]
    y = now[0]
    if x-1 > -1:
        if maps[y][x-1]==0:
            stack.append([y, x-1])
            maps[y][x-1]=2
    if x+1 < hori:
        if maps[y][x+1]==0:
            stack.append([y, x+1])
            maps[y][x+1]=2
    if y-1 > -1:
        if maps[x][y-1]==0:
            stack.append([x, y-1])
            maps[x][y-1]=2
    if y+1 < hori:
        if maps[x][y+1]==0:
            stack.append([x, y+1])
            maps[x][y+1]=2
return False
   
