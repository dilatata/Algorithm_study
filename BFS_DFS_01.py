# 깊이우선 탐색
# 너비우선탐색

'''
깊이우선탐색 DFS
Depth First Search / 넓이 우선 탐색을 의미
하나의 경우의 수에 대해서 모든 경우의 수를 조사하고 다음 경우의 수를 조사하면서 해를 찾는 과정
하나의 트리구조 -> 하나의 길을 끝까지 확인 후 다른 길 조사

- 깊이 우선 탐색과 스택
검사중 a
아래 bcd 스택에 넣기
a 정답이 아님
스택 상위의 b 검사
b 하위 ef 스택에 넣기
b 정답 아님
스택 상위 e 검사
e 하위 j 스택에 넣기
e 정답 아님
j 검사
j 하위 스택 없으므로 스택에 추가 없음
스택 상위 f 검사
f정답 아님
f 하위 kl 스택에 추가
....
정답에 도달할 때까지 반복

=====
예시 문제 : 미로찾기
탈출 가능 true
탈출 불가능 false

이동 가능한 길 0
이동 불가능한 길 1

문제를 풀기위해 index 지정
문제를 풀기위해 stack 
검사를 위한 조건문
이동 가능한 좌표 (0,0)으로 시작

'''


while len(stack)>0: # 스텍에 데이터가 있다면
    now = stack.pop() # 스텍에서 가장 마지막 데이터를 추출
    if now == dest: # 정답 여부 검사
        return True # 만약 도착지점이라면 True 반환
    x = now[1]
    y = now[0]
    if x-1 > -1: # 왼쪽으로 이동할 수 있다면 
        if maps[y][x-1]==0: #갈 수 있는 길이라면 스텍에 추가하고 방문여부를 2로 표시
            stack.append([y, x-1])
            maps[y][x-1]=2
    if x+1 < hori: # 오른쪽으로 이동할 수 있다면
        if maps[y][x+1]==0: # 방문여부 체크
            stack.append([y, x+1])
            maps[y][x+1]=2
    if y-1 > -1: # 위쪽으로 이동할 수 있다면
        if maps[x][y-1]==0: # 방문여부 체크
            stack.append([x, y-1])
            maps[x][y-1]=2
    if y+1 < hori: # 아래쪽으로 이동할 수 있다면
        if maps[x][y+1]==0: # 방문여부 체크
            stack.append([x, y+1])
            maps[x][y+1]=2
return False # 스텍에 데이터가 없다면 False 반환


'''
너비우선 탐색 BFS
Breadth First Search / 넓이 우선 탐색
하나의 경우의 수에 대한 다음 단계의 모든 경우이 수를 조사하면서 해를 찾는 과정

A -> B,C,D ->  E,f, 정답 => 알고리즘 종료

너비우선 탐색과 큐
큐 선언
반복문 생성
A 검사 -> 정답아님
A 하위의 BCD 큐에 넣기
A 검사 종료
먼저 들어간 B 부터 검사  -> 정답아님 
B 하위의 EF 큐에 넣기
B 검사 종료
C 검사  -> 정답아님
C 하위 데이터 큐에 넣기
C 검사 종료
....
정답을 얻으면 알고리즘 종료


=====
문제 예제
최단 경로 찾기
- 1번  섬에서부터 12번 섬까지 가는 최단 경로는 얼마인가? 
(모든 경로의 거리는 1이라고 가정)

큐 션언
데이터 검사 조건문 생성
시작점 1에서 시작
+ 1번섬과 검사하고 있는 섬의 거리에 대한 변수 지정 필요 

'''

while len(queue)>0: # 큐에 데이터가 있다면
    count = len(queue) # 같은 거리에 있는 큐 테이터 갯수
    for time in range(count): # 같은 거리에 있는 큐 개수만큼 검사
        now = queue.pop(0)
        if now == dest: #정답이 존재하면 값 반환 + 알고리즘 종료
            return answer
        for i in data: # 연결된 포인트 완전 탐색
            if i[0]==now and visited[i[1]-1]==False: # 방문하지 않은 연결된 길이라면 큐에 추가하고 방문 표시
                queue.append(i[1]) 
                visited[i[1]-1]=True
            elif i[1] == now and visited[i[0]-1]==False:
                queue.append(i[0])
                visited[i[0]-1]=True
    answer+=1 # 하나의 탐색(for문이) 끝났다는 것은 첫번째 섬과의 거리가 1만큼 멀어졌음을 의미
return asswer 
