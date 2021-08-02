'''
해시란 데이터를 다루는 기법 중 하나
검색과 저장이 아주 빠르게 진행된다.
key value값이 한 쌍으로 존재
key 값이 배열의 인덱스로 변환되기 때문
'''

# 딕셔너리 클래스 활용
hash = dict()   # hash = ()
hash[1] = 'apple'
hash['banana'] = 3
hash[(4,5)] = [1,2,3]
hash[10] = dict({1:'a', 2:'b'})
# 배열과 집합은 key 값으로 사용할 수 없음 -> 집합[]과 배열{}은 hash 함수에 의해 index로 변환될 수 없기 때문

# 딕셔너리 수정 -> 재삽입 작업
hash[1] = 'melon'
hash['banana'] = 10

# 딕셔너리 값 추출 pop() 사용
hash.pop(1)
# pop() 사용시 해당 값이 딕셔너리에서 빠져나옴
hash.pop('banana')
hash.pop((4,5))
hash(10)

# 추출하지 않고 data 삭제 -> del() 사용
del hash[1]
del hash['banana']
del hash[(4,5)]
del hash[10] 

# 딕셔너리 활용 1. 딕셔너리 루프 2. 딕셔너리 정렬
hash = dict()
hash.keys() # 모든 key값을 list와 유사한 형태로
hash.values() # 모든 value값을 list와 유사한 형태로
hash.items() # 모든 key and value값을 tuple과 유사한 형태로

hash = dict()
for i in range(1,6):
    hash[i]=i**2

for k in hash.keys():
    print(k)

for v in hash.values():
    print(v)

for i in hash.items():
    print(i)

# 딕셔너리 정렬 sorted() -> 항상 list 타입으로 반환
hash = dict({1:10,3:12,5:7,7:6,4:5})
# keys
sorted(hash.keys(),key=lambda x:x)
# values
sorted(hash.values(),key=lambda x:x)
# keys, values
# key 값에 의한 오름차순 정렬 tuple 형태 
sorted(hash.items(), key=lambda x:x)

# 내림차순
# keys
sorted(hash.keys(), key=lambda x:-x)
# values
sorted(hash.values(),key=lambda x:-x)
# keys, values
# key 값에 의한 내림차순 정렬 tuple 형태 
sorted(hash.items(), key=lambda x:-x) 
# ERROR
# 오름차순의 경우 lambda의 인자값 x가 tuple이였기 때문에 오름차순이 되었던 것
# 하지만 tuple에 - 줄 수 없으므로 

sorted(hash.items(), key=lambda x:-x[1]) 
# x[0], x[1] = key 오름차순, value 오름차순
# -x[0], -x[1] = key 내림차순, value 내림차순
# x[1], x[0] = value 오름차순,  key 오름차순
# -x[1], -x[0] = value 내림차순,  key 내림차순
