# 프로그래머스 주식가격 풀이    
# 초 단위로 기록된 주식가격이 담긴 배열 prices
# 가격이 떨어지지 않은 기간은 몇 초인지를 return
# -> 주식 시장에서 초당 가격 변화값을 입력
# prices = [1,2,3,2,3] 라고 생각해보자

'''
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// prices_len은 배열 prices의 길이입니다.
int* solution(int prices[], size_t prices_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(1);
    return answer;
}

'''

prices = [1,2,3,2,3]

def solution(prices):
    answer = [0]*len(prices) #answer = 0*prices의 길이 = 0이 5개 -> [0,0,0,0,0]
    for i in range(len(prices)-1): # len(price) -1 은 4이므로 range(3)은 0, 1, 2, 3
        for j in range(i+1, len(prices)): #i+1 -> 1, 2, 3, 4 / range(i+1, len(prices)) 는 1, 2, 3, 4 의 값을 갖는다
            answer[i] += 1 # i의 인덱스에 해당하는 데이터에 1 더하기
            if prices[i] > prices[j]: # i 값이 j 값보다 크다면
                break #멈춰라
            else:
                continue # loop 반복
    return answer

# print(solution(prices)) 