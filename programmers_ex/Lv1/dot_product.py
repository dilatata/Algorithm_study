'''
프로그래머스 내적
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

제한사항
a, b의 길이는 1 이상 1,000 이하입니다.
a, b의 모든 수는 -1,000 이상 1,000 이하입니다.
'''
# 입출력 예
'''
a
[1,2,3,4]
[-1,0,1]

b
[-3,-1,0,2]
[1,0,-1]

return
3
-2
'''
# logic 생각하기
'''
a와 b의 길이는 같다.
내적값들을 저장하고 더해줄 변수 k 생성 
k = 0
정해진 길이만큼 내적을 반복하는 코드
 for i in n:
    k += a[i]+b[i]
        k += a[0]+b[0]
        k += a[1]+b[1]
        k += a[2]+b[2]
        ...
        k += a[n-1]+b[n-1]
n = len(a)
    
'''

a = [1,2,3,4]
b = [-3,-1,0,2]
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
        # print(a[i], b[i], answer)
    return answer 

# print(solution(a, b))

# zip 사용
def solution2(a, b):
    return sum([x*y for x, y in zip(a,b)])

# print(solution2(a, b))

# lambda 
solution = lambda x, y: sum(a*b for a, b in zip(x, y))