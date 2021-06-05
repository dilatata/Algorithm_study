from queue import Queue
from typing import Container

# stack 은 쌓다 라는 개념

# python 직접 구현

class Stack(list):
    push = list.append

    def peek(self):
        return self[1]
        

# push 넣다라는 개념 

s = Stack()

s.push(1)
s.push(5)
s.push(10)


# peek 맨 나중에 넣은 값을 보는것 
def peek(self):
    return self[-1]


s= []
s.append(1)
s.append(2)
s.append(5)
#print(s)   ## 1, 2, 5

# pop 가장 마지막에 넣은 값을 호출
s.pop()  # -> 5
#print(s)  # -> [1.2]



## Queue  일이 처리되기를 기다리는 리스트의 의미
## 선착순

class Queue(list):
    put = list.append

    def peek(self):
        return self[0]

    def get(self):
        return self.pop(0)


q  = Queue()

q.put(1)
q.put(2)
#print(q)  # 1,2
q.get() # 1
#print(q) # 2
q.peek()  # 2

d = []

d.append(1)
d.append(2)
d.append(5)
#print(d) # 1, 2, 5
d.pop(0) # 2, 5
d[0]
