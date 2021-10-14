
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


