'''
[문제]
지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다. 이때, A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성해 주세요.
만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.


[제한사항]
지점갯수 n은 3 이상 200 이하인 자연수입니다.
지점 s, a, b는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.
즉, 출발지점, A의 도착지점, B의 도착지점은 서로 겹치지 않습니다.
fares는 2차원 정수 배열입니다.
fares 배열의 크기는 2 이상 n x (n-1) / 2 이하입니다.
예를들어, n = 6이라면 fares 배열의 크기는 2 이상 15 이하입니다. (6 x 5 / 2 = 15)
fares 배열의 각 행은 [c, d, f] 형태입니다.
c지점과 d지점 사이의 예상 택시요금이 f원이라는 뜻입니다.
지점 c, d는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.
요금 f는 1 이상 100,000 이하인 자연수입니다.
fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다.
출발지점 s에서 도착지점 a와 b로 가는 경로가 존재하는 경우만 입력으로 주어집니다.


[입출력 예]
n	s	a	b	fares	result
6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	18
'''


# 다른코드분석

graph=[[]]
 #사전 graph 작업
def pre(n,fares):      
    global graph
    graph=[[100000001 for col in range(n+1)]for i in range(n+1)]
    for i in range(n+1):
        for k in range(n+1):
            if i==k:
                graph[i][k]=0
            elif i==0 or k==0:
                graph[i][k]=0
    for i in fares:
        graph[i[0]][i[1]]=i[2]
        graph[i[1]][i[0]]=i[2]
#가장 비용이 적은 노드 찾는 함수
def minnode(v,f):#방문하지 않은 노드들 중 최단거리의 노드를 구함
    ans=0
    min=100000001
    for i in range(1,len(v)):
        if f[i]<min and v[i]==False:
            min=f[i]
            ans=i
    if ans==0:#연결할수 있는 최단거리 노드가 존재하지 않는 경우
        return -1
    else:
        return ans


def dijk(start,fin,n):#다익스트라알고리즘
    if start==fin:
        return 0
    else:
        global graph
        flist=[0 for i in range(n+1)]
        visit=[False for i in range(n+1)]
        for i in range(1,(n+1)):
            if i==start:
                flist[i]=(100000001)
                visit[i]=(True)
            elif graph[start][i]!=100000001:
                flist[i]=(graph[start][i])
            else:
                flist[i]=100000001
        rc=True
        while visit[fin]!=True:
            curr=minnode(visit,flist)
            if curr==-1:
                rc=False
                break
            else:
                visit[curr]=True
                for i in range(1,n+1):
                    if flist[curr]+graph[curr][i]<flist[i] and visit[i]==False:
                        flist[i]=flist[curr]+graph[curr][i]
        if rc==False:
            return 100000001
        elif rc==True:
            return flist[fin]
def solution(n, s, a, b, fares):
    answer = 100000001
    if len(fares)==3:
        answer=fares[0][2]+fares[1][2]+fares[2][1]
    else:
        pre(n,fares)
        for i in range(1,n+1):
            answer=min(answer,dijk(s,i,n)+dijk(i,a,n)+dijk(i,b,n))
    return answer