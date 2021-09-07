'''
문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
입출력 예
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
'''

'''
이어지는 길
2개 같은 것끼리 이어짐
같은 자리, 같은 값 => 1 -> 합쳤을때 2이면 answer +1

hit
hot
dot / dog
lot / log
      cog
'''


# 도전1
def solution(begin, target, words):
    answer = 0
    begin_lst = list(begin) 
    # print(begin_lst) # h, i, t
    if target not in words: # list에 없는 단어는 반환 X
        return 0 
    else:
        # return 1 # 
        for word in words:
            # print(word)
            word_lst = list(word) 
            # print(word_lst) # ['h', 'i', 't']/['h', 'o', 't']/['d', 'o', 't'],, 반복문 통해서 나옴
            if not word_lst[0] == begin_lst[0] or word_lst[1] == begin_lst[1] or word_lst[2] == begin_lst[2]:
                answer += 1
                begin_lst = word_lst
                # words.pop(word) # TypeError: 'str' object cannot be interpreted as an integer
                words.remove(word)
                print('words:',words, 'answer:', answer)
        # print(words)
    return answer

    # if 단어 길이가 3 이상이면 성립 X -> for 문에 range(len(words)) 넣어서 


# 도전2
def solution(begin, target, words):
    answer = 0
    begin_lst = list(begin) 
    # print(begin_lst) # h, i, t
    if target not in words: # list에 없는 단어는 반환 X
        return 0 
    else:
        # return 1 # 
        for word in words:
            # print(word)
            word_lst = list(word) 
            # print(word_lst) # ['h', 'i', 't']/['h', 'o', 't']/['d', 'o', 't'],, 반복문 통해서 나옴
            if not word_lst[0] == begin_lst[0] or word_lst[1] == begin_lst[1] or word_lst[2] == begin_lst[2]: # 여기가 꼬였어
            count=0
            for i in range(len(word_lst)):
                if  word_lst[i] == begin_lst[i]:
                    count += 1
                    # print(count)
                    if count ==2:
                        answer += 1
                        print(word_lst)
                        begin_lst = word_lst
                        # words.pop(word) # TypeError: 'str' object cannot be interpreted as an integer
                        words.remove(word)
                        # print('words:',words, 'answer:', answer)
        # print(words)
    return answer

    # if 단어 길이가 3 이상이면 성립 X -> for 문에 range(len(words)) 넣어서 
    # 뭔가 더 단단히 꼬였다.

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"] # 1
print(solution(begin, target, words))


# 참고 코드1
def solution(begin, target, words):
    answer = 0
    queue = [begin]
    while True:
        tmp_q = []
        for word_1 in queue:
            if word_1 == target:
                return answer
            for word_2_idx in range(len(words)-1, -1, -1): # 해당 방식 사용하면 index오류 없이 pop()사용 가능
                word_2 = words[word_2_idx]
                difference = sum([x != y for x, y in zip(word_1, word_2)])
                if difference == 1:
                    tmp_q.append(words.pop(word_2_idx))
        if not tmp_q:
            return 0
        queue = tmp_q
        answer += 1


# 참고 코드 2
def solution3(begin, target, words):
    answer = 0
    stacks = [begin]
    visited = {i:0 for i in words} # 이미 검사했던 단어를 다시 검사하지 않도록 하기 위해서
    if target not in words:
        return 0
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for word in words:
            for i in words:
                for i in range(len(word)):
                    copy = list(word)
                    copy_front = list(stack)
                    copy[i] = 0
                    copy_front[i] = 0
                    if copy == copy_front:
                        if visited[word] != 0: # visited가 1이라면 이미 검사했던 단어
                            continue
                        visited[word] = 1 # visited 가 0이면 해당 단어의 visited값을 1로 변경
                        stacks.append(word)
                        break
        answer += 1 # Depth 1추가
    return answer