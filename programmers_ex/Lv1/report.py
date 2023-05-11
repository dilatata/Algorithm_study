def solution(id_list, report, k):
    answer = []
    report_case = dict()
    report_count = dict()
    reported_count = {}

    for i in range(len(id_list)):
        report_count[id_list[i]] = 0
        reported_count[id_list[i]] = 0
        report_case[id_list[i]] = ''

        
    for i in range(len(report)):
        a, b = report[i].split()
        
        # 신고 목록 작성
        if len(report_case[a]) == 0 :
            report_case[a] = b
        else:   
            report_case[a] = report_case.get(a) +','+ b
        
    # 중복 신고 확인
    check_list=[]
    for i in id_list:
        check_list = report_case[i]
        check_list = check_list.split(',')
        report_case[i] = list(set(check_list))
    
    count_list=[]
    for i in id_list:
        count_list = report_case[i]
        for b in count_list:
            if b != '': #없으면 keyerror='' 발생
                report_count[b] = report_count[b] + 1
        
    reported_list=[]
    # k 값과 비교, 신고자 확인
    for i in id_list:
        if report_count[i] < k:
            continue
        else:
            reported_list.append(i)
            
    # reported count
    for i in id_list:
        report_list = report_case[i]
        for m in report_list:
            if m in reported_list:
                reported_count[i] = reported_count[i] + 1
            
    answer = list(reported_count.values())

    return answer