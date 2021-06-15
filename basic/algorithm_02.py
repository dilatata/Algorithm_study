'''
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, 
solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다. n길이에 맞춰서 slice
입출력 예
n	return
3	"수박수"
4	"수박수박"
'''
'''
list = '수박*5000' '수박'으로 문자열 10000개짜리 리스트 만들기
def solution(n):
    answer = '수박수박수박수박.....'[0:n자리 만큼 잘라주기]
    return answer
'''



def solution(n):
    watermelon = '수박'*5000
    answer = watermelon[0 : n]
    return answer

# print(solution(3))
# print(solution(4))