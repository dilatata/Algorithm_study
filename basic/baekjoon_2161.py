
'''
문제
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.

N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(1≤N≤1,000)이 주어진다.

출력
첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
'''

# 내가 만든 거
def solution(n):
    answer = []
    l =[]
    for i in range(1, n+1):
        l.append(i)
    while len(l) > 1:
        answer.append(l.pop(0))
        l.append(l.pop(0))

    answer.append(l.pop(0))
    return answer

print(solution(7))


# #구글링
N = int(input())
card_list = [i for i in range(1, N+1)]
discarded_card = []

while len(card_list) != 1:
    discarded_card.append(card_list.pop(0)) #버리기
    card_list.append(card_list.pop(0)) #뒤로 옮기기

for i in discarded_card:
    print(i, end = ' ')
print(card_list[0])

#구글링2 deque 사용

from collections import deque

n = int(input())
cards = deque(list(range(1, n+1)))
res = []
while cards:
    card = cards.popleft()
    res.append(card)
    if cards:
        card = cards.popleft()
        cards.append(card)
print(*res) # print(*list명/tuple명/set명) : 값만 호출할 때 사용, print(*dict명) : key 값 모두 호출할 때 사용
print(res) 




# rest = {1 : 2, 4 : 3}
# print(type(rest))
# print(*rest)
# print(rest)