'''
프로그래머스 최소직사각형 만들기
모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

제한사항
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.
'''
# 입출력 예
'''
sizes	
[[60, 50], [30, 70], [60, 30], [80, 40]]
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

result
4000
120
133
'''

# logic 생각하기
'''
1. 가로 세로 중에 큰수와 작은 수 나눠서 모으기
2-1. 큰 수 중 가장 큰 수
2-2. 작은 수 중 가장 큰 수
'''

sizes= [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

# 1. 
def solution(sizes):
    b = []
    s = []
    for i in sizes:
        # print (i, i[0], i[1])
        if i[0] > i[1]: # 가로가 긴 명함
            b.append(i[0])
            s.append(i[1])
        elif i[0] < i[1] : # 세로가 긴 명함
            b.append(i[1])
            s.append(i[0])
        else: # 정사각형의 명함
            b.append(i[0])
            s.append(i[0])

    answer = max(b)*max(s)
    return answer

# print(solution(sizes))

# solution2 return 값에 모두 넣기
'''
for i in sizes 라고 할 때 i 속의 큰 수와 작은 수 중 큰 값을 찾는 것
max(max(i))
max(min(i))
'''
def solution2(sizes):
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)

# print(solution2(sizes))

