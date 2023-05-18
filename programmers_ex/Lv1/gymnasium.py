def solution(n, lost, reserve):   
    reserve_st = set(reserve)-set(lost)
    lost_st = set(lost) - set(reserve)
    
    for i in reserve_st:
        if i-1 in lost_st:
            lost_st.remove(i-1)
            
        elif i+1 in lost_st:
            lost_st.remove(i+1)
    answer = n - len(lost_st)

    return answer