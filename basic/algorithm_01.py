'''
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

for in range
sum

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요. if a == b
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다. 
a와 b의 대소관계는 정해져있지 않습니다. if a>b/ elif a<b

입출력 예
a	b	return
3	5	12
3	3	3
5	3	12
'''
'''
def solution(a, b):
더한 값을 받을 변수

a와 b 사이 대소비교
    for k in range(a와 b 사이 값들찾기):
        변수에 값 하나하나 더해주기

return 변수
'''

def solution(a, b):
    sum1 = 0
    if a > b:
        for i in range(b, a+1):
            sum1 = sum1 + i
    elif a < b:
        for i in range(a, b+1):
            sum1 = sum1 + i
    else:
        sum1 = sum1 + a
    return sum1


# a = 3
# b = 5
# print(solution(a, b))