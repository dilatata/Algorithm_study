'''
부족한 금액 계산하기
놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.

제한사항
놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
'''
# 입출력 예
'''
price 3
money 20
count 4
result 10
'''
# logic 생각하기
'''
1*price - 2*price ..... -n*price - money >= 0 
price(1+2+3+...+n) - money  = r
price(1~n까지의 합) - money  = r


1. 1~n까지의 합 찾기
    t = 0
    for i in range(1, n+1):
        t += i
    
2. result(부족한 값)
    t*price - money

'''
from programmers_ex.min_rectangle import solution2


price = 3
money = 20
count = 4

def solution(price, money, count):
    t = 0
    for i in range(1, count+1):
        t += i
    # print(t)
    r = t*price - money

    if r <= 0: # 소지금액이 부족하지 않은 경우
        answer = 0
    else: # 소지금액이 부족한 경우
        answer = r

    return answer

# print(solution(price, money, count))