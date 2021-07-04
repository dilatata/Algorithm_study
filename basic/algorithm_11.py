'''
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
입출력 예
arr1	        arr2	        return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	    [[3],[4]]	    [[4],[6]]
'''
'''
list1 = [1,2]
list2 = [2,3]
list3 = list1 + list2
print(list3) [1, 2, 2, 3]
-> list의 index 지정해서 합하기
-> 행렬은 numpy 쓰면 빠른데
'''

import numpy as np 

arr1 = [[1,2],[2,3]]
arr2=[[3,4],[5,6]]

# arr3 = [[3],[2]]
# arr4 = [[4],[5]]

def solution(arr1, arr2):
    answer = [[]]
    answer = np.array(arr1)+np.array(arr2)
    return answer

# print(solution(arr3,arr4))


# ----------------------

def solution2(arr1, arr2):
    for i in range(len(arr1)):
        for k in range(len(arr1[i])):
            arr1[i][k] = arr1[i][k] + arr2[i][k]
            return arr1


print(solution2(arr1,arr2))
