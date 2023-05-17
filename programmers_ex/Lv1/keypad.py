
def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    middle = [2,5,8,0]
    phone_dict = {1:[3,0], 2:[3,1], 3:[3,2],4:[2,0], 5:[2,1], 6:[2,2],7:[1,0], 8:[1,1], 9:[1,2],'*':[0,0], 0:[0,1], '#':[0,2]}
    l_now = phone_dict['*']
    r_now = phone_dict['#']
    
    for i in numbers:
        now = phone_dict[i]
        if i in left:
            answer += 'L'
            l_now = now
            
        elif i in right:
            answer += 'R'
            r_now = now
            
        elif i in middle:
            l_d=0
            r_d=0
            
            # 거리계산
            for a,b,c, in zip(l_now, r_now, now):
                l_d += abs(a-c)
                r_d += abs(b-c)
                
            if l_d < r_d:
                answer += 'L'
                l_now = now
    
            elif l_d > r_d:
                answer += 'R'
                r_now = now
                
            else:
                if hand == 'left':
                    answer += 'L'
                    l_now = now
                elif hand == 'right':
                    answer += 'R'
                    r_now = now
    return answer
