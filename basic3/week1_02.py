'''
문제
최백준 조교는 사실 엄청난 갑부다. 그는 그 사실을 숨겼지만 어느 날 김재홍 조교에게 그 사실을 발각당한다. 결국 최백준 조교는 가지고 있는 돈을 몽땅 동전으로 바꾸어서 땅에 묻어 둘 생각을 하게 된다.

하지만 최백준 조교가 가진 돈이 워낙 많기 때문에 돈을 묻어두어도 그 위치가 김재홍 조교에게 발각될 위험이 있다.

그 때문에 그는 최소의 동전 개수로 돈을 바꾸고 싶다.

최백준 조교는 엄청난 구두쇠이기 때문에 돈이 단 1원도 줄거나, 심지어는 늘어나는 것도 싫어한다.

정확히 그가 가진 금액을 동전으로 교환하되, 그 개수를 최소화하는 방법을 찾도록 하자.

입력
첫째 줄에는 엄청난 갑부인 최백준 조교가 가진 돈의 금액(109 ≤ M ≤ 1018)이 주어진다. 두 번째 줄에는 동전의 종류 N(1 ≤ N ≤ 1,000)이 주어진다. 세 번째 줄에는 동전의 금액 Ai (1 ≤ Ai ≤ 10,000)가 N개 주어진다.

N가지의 동전 중 1원짜리 동전은 항상 있기 때문에, 금액을 못 만드는 경우는 없다.

출력
동전으로 딱 맞는 금액을 만들 때, 그 최소 개수를 출력한다.

예제 입력 1 
1000000001
2
10000 1
예제 출력 1 
100001
'''

# 도전

tot = int(input())
k = int(input())
coins = list(map(int,input().split()))
# print(tot, k, coin, type(coin)) # 1000000001 2 ['10000', '1'] <class 'list'>
print(coins)
# coins = coins.sort(reverse=True) # 최소 coin 수 만들기 위해서 큰 금액 먼저 계산
# coins = sorted(coins)
coins.sort(reverse=True)

'''
list.sort() : 원본 리스트의 순서 변환 , 새로운 변수에 대입 필요 X
sorted(list) : 정렬된 새로운 리스트 반환 , 사용시 새로운 변수에 대입
차이에대한 정의 정확하게 하기!
'''
# print(coins)
# TypeError: 'NoneType' object is not iterable 문제 해결하기
# print(coins, type(coins))

answer = 0
for coin in coins:
    # print(coin, type(coin))
    # coin = int(coin) # map 사용해서 필요 없어짐
    if coin <= tot:
        ans=tot//coin 
        # print('ans:', ans)
        tot=tot-ans*coin
        answer += ans
    
print(answer)
            
