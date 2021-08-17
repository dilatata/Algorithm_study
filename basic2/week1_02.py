'''
문제
태균이는 지금 태권도 겨루기 중이다. 
지금은 상대에게 지고 있지만 지금부터 진심으로 경기하여 빠르게 역전을 노리려 한다.

태균이가 현재 할 수 있는 연속 발차기는 두가지가 있다.

A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 
하지만 상대 역시 3점을 득점하는 위험이 있다.
B는 1점을 얻는 연속 발차기이다.
현재 태균이의 점수 S와 상대의 점수 T가 주어질 때, S와 T가 같아지는 최소 연속 발차기 횟수를 구하는 프로그램을 만드시오.

입력
첫째 줄에 테스트 케이스의 수 C(1 ≤ C ≤ 100)이 주어진다. 둘째 줄부터 C줄에 걸쳐 테스트 케이스별로 현재 점수 S와 T가 공백을 사이에 두고 주어진다. (1 ≤ S < T ≤ 100)

출력
각 줄마다 S와 T가 같아지는 최소 연속 발차기 횟수를 출력한다.

예제 입력 1 
6
10 20
2 7
15 62
10 37
11 50
34 59
예제 출력 1 
3
3
4
4
5
25
'''

# bfs 구현 예제 : 경로 찾기
# bfs 코드에서 queue는 list 봐 queue모듈을 사용해 구현하는 것이 효율적
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


# 다른 사람 답안

from collections import deque

def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    check = [-1]*(200)
    while q:
        node, t, c = q.popleft()
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c+1))
            q.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    # print(bfs(S, T))



# 망
def solution(S, T):
    s = S
    t = T
    c = 0
    while s != t and s < t:
        if t-(s+1) > t+3-(s*2) and s*2 <= t+3:
            s = s * 2
            t = t + 3
            c = c + 1
            print(s,t,c)
        else:
            s = s +1
            c = c + 1
            print(s,t,c)
    return c 

# print(solution2(10,20))


'''
while s != t:
    if 3 < s and 2*s <= t + 3:
        s = s + s
        t = t + 3
        c = c + 1
        print(s,t,c)
    else:
        s = s + 1
        c = c + 1
        print(s,t,c)
    if s == t or s > t:
        break 
'''


