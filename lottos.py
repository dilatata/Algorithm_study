def solution(lottos, win_nums):
    answer = []
    unknown = lottos.count(0)
    O_num = 0
    for i in range(6):
        if lottos[i] in win_nums:
            O_num += 1
        
    if O_num ==0 and unknown == 0 :
        min_p = 6
        max_p = 6
    elif unknown == 0:
        min_p = 7 - O_num
        max_p = min_p
    elif O_num == 0:
        min_p = 6 - O_num
        max_p = 7 - O_num - unknown
    else: 
        min_p = 7 - O_num
        max_p = 7 - O_num - unknown
        
    answer = [max_p, min_p]
    return answer