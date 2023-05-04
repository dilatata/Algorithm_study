def solution(survey, choices):
    answer = ''

    R = 0
    T = 0
    C = 0
    F = 0
    J = 0
    M = 0
    A = 0
    N = 0
    
    for i in range(len(survey)):
        
        if survey[i] == 'RT':
            if choices[i] - 4 < 0:
                R += 4- choices[i]
            if choices[i] - 4 > 0:
                T += choices[i] - 4
        elif survey[i] == 'TR':
            if choices[i] - 4 < 0:
                T += 4- choices[i]
            if choices[i] - 4 > 0:
                R += choices[i] - 4
        elif survey[i] == 'CF':
            if choices[i] - 4 < 0:
                C += 4- choices[i]
            if choices[i] - 4 > 0:
                F += choices[i] - 4
        elif survey[i] == 'FC':
            if choices[i] - 4 < 0:
                F += 4- choices[i]
            if choices[i] - 4 > 0:
                C += choices[i] - 4
        elif survey[i] == 'JM':
            if choices[i] - 4 < 0:
                J += 4- choices[i]
            if choices[i] - 4 > 0:
                M += choices[i] - 4
        elif survey[i] == 'MJ':
            if choices[i] - 4 < 0:
                M += 4- choices[i]
            if choices[i] - 4 > 0:
                J += choices[i] - 4
        elif survey[i] == 'AN':
            if choices[i] - 4 < 0:
                A += 4- choices[i]
            if choices[i] - 4 > 0:
                N += choices[i] - 4
        elif survey[i] == 'NA':
            if choices[i] - 4 < 0:
                N += 4- choices[i]
            if choices[i] - 4 > 0:
                A += choices[i] - 4
    if R >= T:
        answer += 'R'
    elif T > R:
        answer += 'T'
        
    if C >= F:
        answer += 'C'
    elif F > C:
        answer += 'F'
        
    if J >= M:
        answer += 'J'
    elif M > J:
        answer += 'M'
        
    if A >= N:
        answer += 'A'
    elif N > A:
        answer += 'N'    
    
    return answer
