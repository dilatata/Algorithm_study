'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''
'''
hash 사용해서 풀어보기
participant는
hash()로 넣고 
completion은
hash() 사용해서 지우고
남은 participant return 하도록 만들기 
'''
# 단 한명만 남기 때문에
def solution(participant, completion): 
    answer = '' 
    count = 0 
    dic = {} 
    
    for part in participant: 
        dic[hash(part)] = part 
        count += int(hash(part)) 
    
    for com in completion: 
        count -= hash(com) 
    
    answer = dic[count] 
    return answer



# ========= 확인

participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	
# print(solution(participant, completion))


# ========= 이것 저것 연습
answer = '' 
count = 0 
list=[]
dic = {} 

for part in participant: 
    # print(hash(part),part)
    dic[hash(part)] = part 
    # list.append(hash(part))
    # print(list)
    # count += int(hash(part)) 

print(dic) # {3790566131446044929: 'leo', -9155820316457119863: 'kiki', 7608176301634952774: 'eden'}
# print(count)

for com in completion: 
    dic.pop(hash(com)) 
    # list.pop(hash(part)) -> nono
    # print(list)
    # print(count)
print(dic) # {3790566131446044929: 'leo'}
print(dic.values()) # dict_values(['leo'])


# for i in dic.values():
    # answer += i # leokiki
    # list.append(i)
# print(dic[count])
# return answer
# answer = list[0:]

# answer = dic.values()
# answer = dic[key]
# print(dic[count])
# return answer
# print(answer)