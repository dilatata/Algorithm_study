'''
신규 아이디 추천
7단계의 순차적인 처리 과정
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

[제한사항]
new_id는 길이 1 이상 1,000 이하인 문자열입니다.
new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정
'''
# 입출력 예
'''
no	    new_id	                        result
예1	    "...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	    "z-+.^."	                    "z--"
예3	    "=.="	                        "aaa"
예4	    "123_.def"	                    "123_.def"
예5	    "abcdefghijklmn.p"	            "abcdefghijklmn"
'''
from hashlib import new
from operator import indexOf


new_id= "=.="

# list 만들어서 풀기 
def solution2(new_id):
    sp= ["-", "_", "."]
    
    # step1
    step1 = new_id.lower()
    step2=[]
    step3=[]

    #step2
    for i in step1:
        if i.isalpha():
            step2.append(i)
        elif i.isdigit():
            step2.append(i)
        elif i in sp:
            step2.append(i)
    # print(step2)

    # step3
    for i in step2:
        if i == ".":
            if len(step3) == 0:
                step3.append(i)
            elif len(step3) > 0 and step3[-1] != ".":
                step3.append(i)
        else:
            step3.append(i)
    # print(step3)

    # step4
    if step3[0] == ".":
        step3.pop(0)
    # print(step3, len(step3))

    # step5
    step5=[]
    if len(step3) < 1:
        step5.append("a")
    else:
        step5 = step3
    
    print(step5, len(step5))

    # step6
    if len(step5) > 15:
        step5 = step5[0:15]
    # print(step5)

    while step5[-1] == ".":
        step5.pop()

    #step7
    while len(step5) < 3:
        if step5[-1] == ".":
            step5.pop()
        else:
            step5 += step5[-1]
    

    answer = "".join(step5)
    return answer

# print(solution(new_id))


# 문자열로 바로 풀기
def solution(new_id):
    sp= ["-", "_", "."]
    answer=""
    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in sp:
            answer += i
    
    # 3 ".." -> "."
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4 
    while len(answer) > 1 and answer[0] == ".":
        answer = answer[1:]
    
    while len(answer) > 0 and answer[-1] ==".":
        answer = answer[:-1]

    # 5
    if answer == "":
        answer += "a"

    # 6 
    if len(answer) > 15:
        answer = answer[:15]
        while answer[-1] == ".":
            answer = answer[:-1]

    # 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer

# print(solution(new_id))
