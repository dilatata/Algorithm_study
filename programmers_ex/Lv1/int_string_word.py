'''
숫자 문자열과 영단어
숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성

숫자 영단어 대응
숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

제한사항
1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

제한시간 안내
정확성 테스트 : 10초
'''
# 입출력 예
''' 
s
"one4seveneight"
"23four5six7"
"2three45sixseven"
"123"	

result
1478
234567	
234567
123
'''

def solution(s):
    answer = 0
    return answer