'''
문제

보통 r과 M은 서로소인 숫자로 정하는 것이 일반적이다. 
우리가 직접 정하라고 하면 힘들테니까 r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891(놀랍게도 소수이다!!)로 하자.
이제 여러분이 할 일은 위 식을 통해 주어진 문자열의 해시 값을 계산하는 것이다. 그리고 이 함수는 간단해 보여도 자주 쓰이니까 기억해뒀다가 잘 써먹도록 하자.


입력
첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.
입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.


출력
문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.
'''


L = int(input())
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i) #아스키 코드 값을 돌려주는 ord함수
print(answer % 1234567891)


#========

L = int(input())
M = 1234567891
r = 31
user_input = input()
 
answer = 0
 
for i in range(len(user_input)):
    num = ord(user_input[i]) - 96
    answer += num * (r ** i)
 
print(answer % M)

'''
**문제 풀이
H = (∑ i=0 부터 (l−1) 까지 ai * r^i) mod M
출력과 비교해볼때 a를 기준으로 1로잡고 계산을 해야함을 알 수 있다.
a가 1이고 i번째에 나온다면 a * 31^i이 된다.
그렇다면 우리는 알파벳을 숫자로 바꾸는 것을 먼저 해야한다.
a 기준으로 아스키코드는 97이므로 96을 빼주면 된다.
r = 31로주고 M을 1234567891로 준 뒤
∑alphabet * r ^ i Mod M을 하면된다. 
'''