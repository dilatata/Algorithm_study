def solution(today, terms, privacies):
    answer = []
    # 딕셔너리 만들기 - {'종류':기간, '종류':기간 ...}
    case_dict = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    for term in terms:
        case = term[0]
        case_dict[case] = int(term[2:])
    for i in range(len(privacies)):
        date, case = privacies[i].split()
        i_year, i_month, i_day = int(date[0:4]), int(date[5:7]), int(date[8:])
        
        # 시작 달에 조건 기한 더하기
        i_month += case_dict[case]
        
        # i_month가 12가 넘으면 12만큼 뺴고 i_year에 1 추가하기
        while i_month >12:
            i_month -= 12
            i_year += 1
        
        # 적으면 추가하기
        if i_year < year:
            answer.append(i+1)
           
        elif i_year <=year: # 1
            if i_month < month:
                answer.append(i+1)
                
            elif i_month <= month: #2
                if i_day <=day:
                    answer.append(i+1)
                    
         		# 1, 2 == 로 했을때보다 <= 가 더 속도가 빠르게 나옴
    return answer