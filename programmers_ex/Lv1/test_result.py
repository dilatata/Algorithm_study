def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_a = 0
    count_b = 0
    count_c = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            count_a += 1
        if answers[i] == b[i%8]:
            count_b += 1
        if answers[i] == c[i%10]:
            count_c += 1
    count_dict = {1:count_a, 2:count_b, 3:count_c}
    # max_st = max(count_dict, key=count_dict.get) 여러명이 동점자일경우 해결할 수 없음
    answer = [k for k,v in count_dict.items() if max(count_dict.values()) == v]

    return answer