'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.
'''

'''
def solution(answers):
    answer = []
    return answer
'''

'''
def solution(answers):
    a=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    answer = []
    choice = []
    count = 0
    n = 0
    for i in answers:
        answer.append(i)
    for k in a:
        choice.append(k)
        while n < len(answer):
            if answer[n] == choice[n]:
                count += 1
                n += 1
            else:
                n += 1
        
    return answer

answers=[1,2,3,4,5]
solution(answers)
'''
# solution which is the most similar with the algorythm that I tried to make.
answers=[1,2,3,4,5]


def solution(answers):
    answer = []
    supo = [[1, 2, 3, 4, 5], \
        [2, 1, 2, 3, 2, 4, 2, 5], \
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    right = [0, 0, 0] #정답 개수

    for i in range(len(supo)): #수포자의 수만큼 반복 -> 0, 1, 2 -> 3회
        for j in range(len (answers)): #answers의 수만큼 반복 -> 0, 1, 2, 3, 4 -> 5회
            n = len(supo[i]) # 수포자의 정답 찍는 방법의 수 * answers의 수 -> 10 10 10 10 10 16 16 16 16 16 20 20 20 20 20
            if answers[j] == supo[i][j%n]: # answers의 j인덱스에 해당하는 데이터와 supo의 i인덱스의 인덱서가 j나누기n의 나머지에 해당하는 데이터가 같은 경우  
                right[i] += 1 #right에 i번째 인덱스에 해당하는 데이터에 1을 더해라
        for idx, score in enumerate(rignt): #enumerate() : 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능, idx 와 score정보를 뽑아냄
            if score == max(rignt): #score가 right의 max와 같을 경우
                answer.append(idx+1) #answer에 해당 idx+1값을 할당하라
        return answer

solution(answers)

