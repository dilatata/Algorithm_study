'''
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
"abcde"	"c"
"qwer"	"we"
'''
'''
st
s의 길이 나누기 2의 나머지가 0 이면 짝수
s의 길이 나누기 2의 나머지가 0 이 아니면 홀수
따라 중간 인덱스의 번호를 answer에 넣기

'''

def solution(s):
    answer = ''
    if len(s)%2 == 0:
        answer = s[len(s)//2-1] + s[len(s)//2]
    else:
        answer = s[len(s)//2] 
    return answer

# s = 'abcde'
# print(solution(s))