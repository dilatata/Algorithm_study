def solution(array, commands):
    answer = []
    for i in commands:
        sample_n = array[i[0]-1 :i[1]]
        sample_n.sort()
        target_n = sample_n[i[2]-1]
        answer.append(target_n)
    return answer