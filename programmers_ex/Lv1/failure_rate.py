'''
실패율

스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성

제한사항
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
'''
# 입출력 예
'''
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]
'''

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    l = []
    a = len(stages)
    for i in range(1, N+1): # 1~ N 번
        c = 0 # 해당 레벨에서 실패할 사람의 수
        for j in range(len(stages)): # 도전한 사람들 중에서 확인하기
            if stages[j] == i: # 해당 스테이지에서 실패하면
                c += 1 
        if c == 0:
            l.append(0)
        else:
            l.append(c/a)
        a = a-c # 실패한 사람 수 줄이기
    
    b = sorted(l, reverse=True) # 내림차순 리스트 만들기
    answer = []

    for i in range(len(b)): # 내림차순으로 만든 리스트와 
        answer.append(l.index(b[i])+1) # b[i]값을 같는 인덱스 +1 로 해당 라운드 answer에 넣기
        l[l.index(b[i])] = 2 # 확인된 값은 2로 중복되지 않게 없애기

    return answer

print(solution(N, stages))