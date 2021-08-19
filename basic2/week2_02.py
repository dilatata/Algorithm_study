'''
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
[0, 5, 6, 9, 7, 2, 10] 5
[0, 5, 6, 9, 7, 2, 10, 1, 4, 6, 8] 
'''
# 나의 답안 93.8
def solution(citations):
    answer = 0
    citations.sort()
    for i in citations:
        print('----- i:', i, '------')
        # print(len(citations))
        for a in range(len(citations)):
            # print(a)
            if citations[a] >= i:
                answer += 1
                # print(answer)
            else:
                continue
        if answer <= i :
            return answer
        else:
            answer = 0

# 나의답안2 yeah~~!!
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        h = len(citations)-i
        if citations[i] >= h:
            answer = h
            break
    
    return answer                    

# citations = [3, 0, 6, 1, 5]
# print(solution(citations))
# k = [0, 5, 6, 9, 7, 2, 1, 4, 6, 8,7]
# print(solution(k))

# 다른사람 답안
def solution(citations):
    answer = 0
    # 1. citations을 오름차순으로 정렬합니다.
    citations.sort()
    # 2. citations 길이 n을 구합니다.
    n = len(citations)
    # 3. 0~n까지 다음을 반복합니다
    for i in range(n):
        # 1. hIndex는 n-i입니다.
        hIndex = n-i
        # 2. citations[i]가 hIndex보다 크거나 같으면, answer에 hIndex를 저장하고 반복을 멈춥니다. 
        if citations[i] >= hIndex:
            answer = hIndex
            break
    
    return answer