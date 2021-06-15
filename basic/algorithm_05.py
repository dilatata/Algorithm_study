'''
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,  ->  if문 비교
다르면 False를 return 하는 solution를 완성하세요. 
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. -> p == y == 0,  
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다. -> 대문자 혹은 소문자로 맞춰주기

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
입출력 예
s	answer
"pPoooyY"	true
"Pyy"	false
입출력 예 설명
입출력 예 #1
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.
'''
'''
함수
대소문자 비교를 위해 lower함수 사용해소 모두 소문자로 만들기
문자열 하나하나 나눠서 p와 y 개수 구하기
if문 p와 y의 개수 비교하기
p의 수 == y의 수 -> true
p>y or p<y -> false
그 왜 ->true
리턴 answer 
'''


def solution(s):
    p = 0
    y = 0
    low = s.lower()
    for i in low:
        if i == 'p':
            p += 1
        elif i =='y':
            y += 1
    
    if p == y == 0 :
        answer = True
    elif p == y:
        answer = True
    else:
        answer = False
    
    return answer


# s = 'pPoooyY'
# s2 = 'Pyy'
# print(solution(s))
# print(solution(s2))