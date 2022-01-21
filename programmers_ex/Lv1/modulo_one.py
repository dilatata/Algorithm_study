'''
나머지가 1이 되는 수 찾기
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성

제한사항
3 ≤ n ≤ 1,000,000
'''
# 입출력 예
'''
n
10
12

result
3
11
'''
'''
1. 
n의 값이 3 이상이므로 2부터 n-1의 값까지 나눠보면서 나머지가 1이 나오는 값을 
리스트에 담고
그중 최소 값을 찾기
2. 
n의 값이 3 이상이므로 2부터 n-1의 값까지 나눠보면서 나머지가 1이 되는 수가 나오면 
break 하고 해당 값을 answer로
'''
n = 10

# 1. 
def solution(n):
    a = []
    for i in range(2,n,1):
        if n%i == 1:
            a.append(i)

    print(a)
    answer = min(a)
    return answer

print(solution(n))

