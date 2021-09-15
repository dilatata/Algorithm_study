'''
문제
홍익이는 N x N 전구 판을 가지고 있다. 전구 판에는 각 칸마다 전구가 하나씩 연결되어 있다. 이 전구 판에서 하나의 전구를 누르면, 해당 전구를 포함하여 상하좌우의 총 5개 전구들의 상태가 변화한다. 다시 말해, 5개의 전구들 중 불이 켜져 있던 전구는 불이 꺼지고, 불이 꺼져 있던 전구는 불이 켜진다.

예를 들어, <그림1> 같은 전구 판이 있다고 하자. 0은 전구가 꺼져 있는 것을 의미하고, 1은 전구가 켜져 있는 것을 의미한다.
※ (1, 1)에서 위와 왼쪽에는 전구가 없다. 따라서 밑, 오른쪽, 그리고 자신의 전구 상태만 바뀐다.

홍익이는 현재 전구 판의 상태를 보고 최대한 적은 횟수로 전구들을 눌러 전구판의 모든 전구를 끄고 싶다.

홍익이를 도와서 전구 판의 모든 전구를 끌 수 있는 최소 횟수 B를 알아보자.

만약, 전구를 끌 수 있는 방법이 없다면, -1을 출력하도록 한다.

입력
N
0과 1로 이루어진 NxN 행렬
2 <= N <= 18
출력
B
예제 입력 1 
2
1 1
1 1
예제 출력 1 
4
예제 입력 2 
3
0 0 0
0 0 0
0 0 1
예제 출력 2 
5
예제 입력 3 
5
0 0 0 1 0
1 1 0 1 1
1 1 1 0 1
1 1 0 0 0
0 0 0 0 1
예제 출력 3 
-1

힌트
예제 1: (모든 전구를 다 눌러야한다.)

예제 2: (0,1), (0,2), (1,0), (2,0), (2,2)를 누르면 된다.
'''

# 다른 코드 분석
import sys
input = sys.stdin.readline # input() 대신 사용 -> input()보다 빠른 연산가능
 
n = int(input())
table = []
for i in range(n): # table list 생성
    temp = list(map(int, input().split()))
    table.append(temp) 
 
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 1234
for f in range(1<<n): # 왼쪽으로 1비트 밀때마다 두 배씩 늘어난다
    a=[]
    for i in range(n):
        a.append(table[i][:])
    cnt = 0
 
    for i in range(n):
        if f & (1<<i): # i 번째 스위치를 누른 경우
            cnt += 1 # cnt 1 추가
            for k in range(5): # 5회 반복
                nx = i + dx[k]
                ny = 0 + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    a[ny][nx] = not a[ny][nx]
 
    for i in range(1, n): # y 좌표
        for j in range(n): # x 좌표
            if a[i-1][j]: #바로 윗 전등이 켜져있다면 스위치를 눌러줘야 한다
                for k in range(5):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        a[ny][nx] = not a[ny][nx]
                cnt += 1
 
 
    can = True
    for i in range(n): # n번 반복
        if a[-1][i] == True: # a[-1][i] 존재하면
            can = False # can False 대입
            break # 반복문 빠져나오기
 
    if can: # 위에서 can 값 True 면
        ans = min(cnt, ans)
 
print(ans if ans != 1234 else -1) # can False 면 -1