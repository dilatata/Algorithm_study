'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 
이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''
'''
첫째 줄 n
n개의 수 입력
m
m개의 수 입력 

m개의 수를 갖는 리스트와 
n개의 수를 갖는 리스트 비교
m[i] == n 이라면 
n[i]에 1씩 더한다.
'''
'''
입력예제
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

출력예제
3 0 0 1 2 0 0 2
'''

first = input()
# print(first, type(first)) #10 <class 'str'>
second = list(input().split(' '))
# print(second, type(second)) # <class 'list'>
third = int(input()) 
forth = list(input().split(' '))


def coun():
    # result = [0]*third
    result = ''
    for i in range(len(forth)):
        count=0
        for j in second:
            if j == forth[i]:
                count += 1
                # result[i] += 1
        result = result+str(count)+' '                 

    return result

print(coun())







