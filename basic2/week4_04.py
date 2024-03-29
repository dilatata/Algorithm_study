'''
문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

예제 입력 1 
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
예제 출력 1 
4
'''

# 다른사람 코드 분석
n = int(input())
array = []
for i in range(n):
    start, end = map(int, input().split())
    array.append((start,end))
    # 입력, 합치기

array = sorted(array, key=lambda a:a[0])
# print(array) # 시작 시간 기준 정렬 확인
array = sorted(array, key=lambda a:a[1])
# print(array) # 종료 시간 기준 정렬 확인
# 가장 많은 회의를 하기 위해서는 끝시간을 기준으로 정렬

end_time = 0
count = 0
for i in array:
    # array에서 i 반복
    if i[0] >= end_time:
        # 첫시작을 0 기준으로 조건문 생성. 문제에서 시작시간과 종료시간 같은 경우도 있으므로 >=
        end_time = i[1]
        # i[0]이 end_time보다 크거나 같다면 end_time이 i[1]이되고
        count +=1
        # 회의 수는 count가 1이 증가
print(count)



# 다른 코드
n = int(input())
time_list = [[0]*2 for i in range(n)]
# 0으로 차있는 2차월 리스트 생성
for j in range(n):
    start, end = map(int, input().split())
    time_list[j][0] = start
    time_list[j][1] = end
time_list.sort(key=lambda x:(x[1],x[0]))
# 시작 시간과 끝 시간 삽입, key 사용해서 정렬 
# x[1],x[0] : 끝시간 기준으로 오름치순 정렬 후 시작시간 오름차순으로 정렬 의미

cnt = 1
end_time = time_list[0][1]
for k in range(1,n):
    if time_list[k][0] >= end_time:
        cnt += 1
        end_time = time_list[k][1]
        # 원소의 시작시간이 끝 시간보다 크거나 같으면 cnt 1 더해주고 원소의 끝시간 새로이 설정
print(cnt)

 
# 정렬 코드 예시
a = [[0,3],[8,5],[8,4],[1,3],[11,14],[3,8],[4,7],[1,5],[3,5]]
#  [[0, 3], [8, 5], [8, 4], [1, 3], [11, 14], [3, 8], [4, 7], [1, 5], [3, 5]]
 
a.sort(key=lambda x:x[0])
# [[0, 3], [1, 3], [1, 5], [3, 8], [3, 5], [4, 7], [8, 5], [8, 4], [11, 14]]

a.sort(key=lambda x:x[1])
# [[0, 3], [1, 3], [8, 4], [1, 5], [3, 5], [8, 5], [4, 7], [3, 8], [11, 14]]


a.sort(key=lambda x:(x[1],x[0]))
# [[0, 3], [1, 3], [8, 4], [1, 5], [3, 5], [8, 5], [4, 7], [3, 8], [11, 14]]

a.sort(key=lambda x:(x[1],-x[0]))
# [[1, 3], [0, 3], [8, 4], [8, 5], [3, 5], [1, 5], [4, 7], [3, 8], [11, 14]]

a.sort(key=lambda x:(x[0],x[1]))
# [[0, 3], [1, 3], [1, 5], [3, 5], [3, 8], [4, 7], [8, 4], [8, 5], [11, 14]]