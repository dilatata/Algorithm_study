'''
3진법 뒤집기
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
'''
# 입출력 예
'''
n 45 125
result 7 229
'''

# logic 생각하기
'''
3진법 -> 수 뒤집기 -> 10진법
3진법 만드는 법: 3으로 나눈 나머지를 역순으로 기재 
    -> 수 뒤집기 안해줘도 되지 않을까?
    1) divmod(n,m) : 사용해서 몫과 나머지 구하기 
    2) a//b, a%b : 몫, 나머지
    while n > 0:
        1) n, result = divmod(n, 3)
        2) result = n%3
            n =  n//3
    n = 0 이 되면 stop 해야하고 얼마나 반복할지 알 수 없으니까 while 사용
10진법 만드는 법 : 
    1) int(string, base)
        int(result, 3) 이때 result 값의 type 이 string 
            -> ''.join(map(str, list))
                이때 list 는 뒤집지 않은 list 사용
    
    2) 계산하기
        a = result[::-1] # list 순서 뒤집기
        Decimal = 0
        for i in a:
            Decimal += a[i]*3**i 
'''

n=125

def solution(n):
    result = []
    while n>0:
        n, re = divmod(n, 3)
        result.append(re)
        print(n)
    print(result)
    a = result[::-1]
    print(a, type(a))
    decimal = 0
    for i in range(len(a)):
        decimal += a[i]*(3**i) 
        print(i,a[i], 3**i, decimal)
    return decimal

# print(solution(n))

# 2
def solution2(n):
    result = []
    while n>0:
        re = n%3
        n = n//3
        result.append(re)
    a = result[::-1]

    decimal = 0
    for i in range(len(a)):
        decimal += a[i]*(3**i) 
        # print(i,a[i], 3**i, decimal)
    return decimal

# print(solution2(n))

# 3.
def solution3(n):
    result = []
    while n>0:
        re = n%3
        n = n//3
        result.append(re)
    a= ''.join(map(str, result))
    print(a)
    decimal=int(a,3)

    return decimal

# print(solution3(n))