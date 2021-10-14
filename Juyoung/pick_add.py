
# https://programmers.co.kr/learn/courses/30/lessons/68644


numbers = [5,0,2,7]

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for k in range(1, len(numbers)):
            if i is not k:
                if numbers[i]+numbers[k] not in answer:
                    answer.append(numbers[i]+numbers[k])
    answer.sort()
    return(answer)

# solution(numbers)
# 성공 ! 


# 다른사람 코드 
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): # 1부터 시작하지 않고 i+1로 i 이후의 인덱스를 갖고오는 게 계산의 수를 줄일 수 있다.
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

# return 에 sorted로 정렬. list(set())으로 중복 삭제 후 list화 를 통한 요약이 가능


# 다른사람 코드2

def solution(numbers): return sorted({numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i>j})

# 1줄로 코드 만들기.......

# 다른사람 코드 3
from itertools import combinations # 여러모로 자주 등장하는 combinations


def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2)) # numbers에서 2개를 짝지어서 생성한 조합을 list로 만듬

    for i in l:
        answer.append(i[0]+i[1]) # 콤비네이션 결과 (list l)로 나온 값들을 각각 더하는 코드
    answer = list(set(answer))
    answer.sort()

    return answer

