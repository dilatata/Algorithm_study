'''
약수의 개수와 덧셈
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성

제한사항
1 ≤ left ≤ right ≤ 1,000
'''
# 입출력 예
'''
left
13
24

right
17
27

result
43
52
'''
# logic 생각해보기
'''
1. left≤ x ≤ rignt 에 해당하는 x 찾기
    for i in range(left,right+1,1):
        a.append(i)
2. 각 x의 약수 개수 찾기
3. 약수의 개수 짝수 홀수 확인
4. 약수의 개수가 짝수면 더하고 홀수면 뺴기
'''
left = 24
right = 27



def solution(left, right):
    a = [] # x에 해당하는 값들의 집합
    b = [] # 약수의 개수 저장하는 집합

    # x값 구하기
    for i in range(left,right+1,1):
        a.append(i)
    # print(a)

    # 약수의 개수 구하기
    for i in range(len(a)):
        a[i]
        count=0
        for k in range(1,a[i]+1):
            if a[i]%k == 0:
                count +=1
        b.append(count)
    # print(b)
         
    answer = 0
    for i in range(len(a)):
        if b[i]%2 == 0: # 짝수
            answer += a[i]
        else: # 홀수
            answer += a[i]*(-1)

    return answer

# print(solution(left, right))


# 다른 코드
'''
약수의 개수가 홀수라면 제곱근을 갖는다.
-> 이걸 이용해서 코드 짜기
'''
def solution2(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

