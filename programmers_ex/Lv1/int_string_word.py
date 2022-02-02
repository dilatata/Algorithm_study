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
# logic 생각하기
'''
1. 영단어 숫자 매칭용 dict 생성 {'영단어': 숫자, ,,,}
2. 매칭된 결과가 문자이면 dict 에서 숫자 찾고 숫자는 그대로 출력
3. answer 문자열로 숫자가 쌓이도록
'''
# s = "2three45sixseven"

def solution(s):
    dict = {}
    numbers=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        dict[numbers[i]]=i
    # print(dict) # {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9} 

    answer = ''
    eng = ''
    for i in s:
        if i.isdigit(): # type 이 숫자인 경우
            answer = answer + i
        elif i.isalpha(): # type 이 알파벳인 경우
            eng = eng + i

            if eng in dict.keys(): # dict에 key 값으로 들어간 영단어와 같은 값이 완성되면
                answer = answer + str(dict[eng])
                eng = '' # eng 초기화
    print(type(answer))
    # return answer
    return int(answer)

# print(solution(s))

s="2onefivethree7"

# 다른 사람 코드

# dict 생성 {str:str,,,,}
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution2(s):
    answer = s
    for key, value in num_dic.items():
        # print(key,value)
        answer = answer.replace(key, value) # replace("찾을값", "변경값",[count])
        # print(answer)
    return int(answer)

# print(solution2(s))

def solution3(s):
    dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(dict)): # 0~9 까지의 숫자를 반복하면서
        s = s.replace(dict[i], str(i)) # dict의 값과 같은 값을 숫자로 변경해서 넣기

    return int(s)

# print(solution3(s))
