'''
없는 숫자 더하기
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성

제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 원소 ≤ 9
numbers의 모든 원소는 서로 다릅니다.
'''
# 입출력 예
'''
number
[1,2,3,4,6,7,8,0] 
[5,8,4,0,6,7,9]	

result 
14
6
'''
# logic 생각하기
'''
numbers 오름차순으로 정렬
0~9 까지의 수 반복
    오름차순 numbers와 비교
        (반복)
        check값 0으로 고정
        같으면 멈추기
        다르면 check(int)에 1 더하기
        -> 0~9의 숫자와 오름차순 numbers가 일치하면 0 값을 갖고 일치하지 않으면 1값을 갖음
    check 의 값을 확인해서 1 값을 갖으면 일치하지 않는 숫자들을 모으는 리스트에 넣기
일치하지 않는 숫자들의 리스트 합 구하기

'''

numbers = [1,2,3,4,6,7,8,0] 
print(type(numbers))
def solution(numbers):
    non=[]
    # sorted_list = sorted(numbers)
    numbers.sort()
    # print(sorted_list)

    for k in range(10):
        # print("k=",k)
        for i in numbers:
            check = 0 
            # print("i=",i)
            if k == i:
                break
            else:
                check += 1
        # print("check=",check)
        if check == 0:
            continue
        else:
            non.append(k)
    print("non=",non)
    answer = sum(non)
    return answer

# print(solution(numbers))
