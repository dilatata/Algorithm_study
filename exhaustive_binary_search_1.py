# 탐색

#데이터 속에서 원하는 데이터를 찾는 것

# 완전탐색, 이분탐색, 깊이우선탐색, 너비우선탐색
# 문자열탐색, kmp, bm

# 완전탐색 : 부르트 포스(brute force)
# 컴퓨터의 빠른 계싼 성능을 활용하여 가능한 모든 경우의 수를 탐색하는 효율성 관점에서 최악의 방법
# 풀리지 않는 문제가 없다는 장점

# 구현방법 

#반복문 , 재귀함수 (동적 계획법, 백트래킹, 탐욕법)

#반복문

def solution(trumo):
    for i in range(len(trump)):
        if trump[i] == 8:
            return i 
    return -1


#재귀함수 -> 다양한 방면에서 활용 가능하나 쉽게 무한루프로 빠지기떄문에 주의 필요

def solution(trump):
    if trump[loc] == 8:
        return loc
    else:
        return solution(trump, loc+1)


#이분탐색

def solution(trump):
    left = 0
    right = len(trump) - 1
    while(left <= right):
        mid = (left+ right)//2
        if trump[mid] == 8:
            return mid
        elif trump[mid] < 8:
            left = mid + 1
        elif trump[mid] > 8:
            right = mid -1
    return mid

