'''
리스트와 내장함수(1)
'''

import random as r

b = list()
# print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b = list(range(1, 11)) # b는 1~10까지의 리스트
# print(b)

c = a + b
# print(c)

# a.pop()  #마지막 원소 뺌
# print(a)
# a.pop(3)
# print(a)

a.remove(4)     #인덱스가 아닌 직접 그 원소 제거
print(a)

print(a.index(5))   #()원소의 index 번호 찾아줌

print(a.index(5))

print(sum(a))
print(max(a))
print(min(a))
print(min(7,5))
print(min(100,115,1115))
print(a)
r.shuffle(a)
print(a)

a.sort(reverse = True)
print(a)
a.sort()
print(a)
a.clear()
print(a)