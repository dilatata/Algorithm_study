'''
문제
KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 
사냥터에 온 사냥꾼은 일직선 상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 
편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ..., xM은 x-좌표 값이라고 하자. 
각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN)과 같이 x,y-좌표 값으로 표시하자. 
동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.

사냥꾼이 가지고 있는 총의 사정거리가 L이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 
단, 사대의 위치 xi와 동물의 위치 (aj, bj) 간의 거리는 |xi-aj| + bj로 계산한다.

예를 들어, 아래의 그림과 같은 사냥터를 생각해 보자. 
(사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 
사정거리 L이 4라고 하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.



사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

입력
입력의 첫 줄에는 사대의 수 M (1 ≤ M ≤ 100,000), 동물의 수 N (1 ≤ N ≤ 100,000), 사정거리 L (1 ≤ L ≤ 1,000,000,000)이 빈칸을 사이에 두고 주어진다. 
두 번째 줄에는 사대의 위치를 나타내는 M개의 x-좌표 값이 빈칸을 사이에 두고 양의 정수로 주어진다. 
이후 N개의 각 줄에는 각 동물의 사는 위치를 나타내는 좌표 값이 x-좌표 값, y-좌표 값의 순서로 빈칸을 사이에 두고 양의 정수로 주어진다. 
사대의 위치가 겹치는 경우는 없으며, 동물들의 위치가 겹치는 경우도 없다. 
모든 좌표 값은 1,000,000,000보다 작거나 같은 양의 정수이다. 

출력
출력은 단 한 줄이며, 잡을 수 있는 동물의 수를 음수가 아닌 정수로 출력한다.

서브태스크
번호	배점	제한
1	9	
M ≤ 10, N ≤ 10, X ≤ 10

2	14	
M ≤ 20, N ≤ 20, X ≤ 20

3	18	
M ≤ 100, N ≤ 100

4	19	
M ≤ 2,000, N ≤ 2,000

5	40	
추가적인 제약 조건은 없다.

예제 입력 1 
4 8 4
6 1 4 9
7 2
3 3
4 5
5 1
2 2
1 4
8 4
9 4
예제 출력 1 
6
예제 입력 2 
1 5 3
3
2 2
1 1
5 1
4 2
3 3
예제 출력 2 
5
'''

# 다른 코드 분석
# 핵심 : 모든 사대가 모든 동물들을 검사하는 대신 각 동물의 가장 가까운 양쪽의 사대를 이분 탐색으로 찾아 사냥할 수 있는지 확인

m, n, l = map(int, input().split())
shooters = list(map(int, input().split()))
animals = []
for _ in range(n):
    x, y = map(int, input().split())
    if y <= l:
        animals.append((x, y))
shooters.sort()
animals.sort(key=lambda axis: axis[0]) # axis[0], 즉 x좌표 기준으로 오름차순 정렬
ans = 0
idx = 0
for i in range(len(animals)):
    left, right = idx, len(shooters)-1
    mid = 0
    while left <= right:
        mid = (left+right)//2
        if shooters[mid] <= animals[i][0]:
            if len(shooters) - 1 == mid or shooters[mid+1] > animals[i][0]:
                break
            left = mid + 1
        else:
            right = mid - 1
    idx = mid
    if abs(animals[i][0] - shooters[mid]) + animals[i][1] <= l: # 양쪽의 사대에서 사격이 가능한 동물일 경우 ans에 1 도한다.
        ans += 1
    elif len(shooters) > mid+1 and abs(animals[i][0] - shooters[mid+1]) + animals[i][1] <= l:
        ans += 1
print(ans)