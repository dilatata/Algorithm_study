'''
문제

인하은행에는 ATM이 1대밖에 없다. 
지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 
사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다. 
예를 들어, 총 5명이 있고, P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자. 
[1, 2, 3, 4, 5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다. 
2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다. 
3번 사람은 1번, 2번 사람이 돈을 뽑을 때까지 기다려야 하기 때문에, 총 3+1+4 = 8분이 필요하게 된다. 
4번 사람은 3+1+4+3 = 11분, 5번 사람은 3+1+4+3+2 = 13분이 걸리게 된다. 
이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.

줄을 [2, 5, 1, 4, 3] 순서로 줄을 서면, 2번 사람은 1분만에, 
5번 사람은 1+2 = 3분, 1번 사람은 1+2+3 = 6분, 4번 사람은 1+2+3+3 = 9분, 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다. 
각 사람이 돈을 인출하는데 필요한 시간의 합은 1+3+6+9+13 = 32분이다. 
이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.

줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.


입력
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)


출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.


예제 입력 1 
5
3 1 4 3 2
예제 출력 1 
32
'''

'''
각 사람이 돈을 인출하는데 필요한 시간의 합이 최솟값이 도기 위해서는 시간을 적게 쓰는 사람부터 인출을 하도록 만들어야 한다.
sort()
총시간이라는 변수 생성
for문을 사람들이 있는 수만큼 반복
1. 사람들이 인출에 사용한 시간을 계산하고 총시간에 누적 합산 
[1,2,3,3,4]
1 + 3 + 6 + 9 + 13 = 32
2. 처음 인출한 사람이 사용한 시간 =  마지막 사람이 기다리는 시간에 포함되므로 총 인원 수 만큼 곱해진다. 라는 계산에서 착안하면
1*5 + 2*4 + 3*3 + 3*2 +4*1 =
5 + 8 + 9 + 6 + 4 = 32
'''

num = int(input())
per_time = list(map(int, input().split()))
# print(per_time)
per_time.sort()
tot_time = 0
for i in range(num):
    tot_time += per_time[i]*(num-i)
    # print(tot_time,'--------')

print(tot_time)