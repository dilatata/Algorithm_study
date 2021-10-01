'''
https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
   
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4

# 필요
1. 3개의 원소의 합 리스트 

2. 소수 확인

'''


# 소수 확인
def prime_num(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num%n == 0:
                return False
        
        return True


# 원소 3개 합 경우 만들기
def solution(nums):
    num=0
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k] 
                if prime_num(num) == True:
                    answer += 1

    return answer