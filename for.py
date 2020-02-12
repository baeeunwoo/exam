'''
반복문
'''


for i in range(10):
    print("hello")

for i in range(10, 0, -3):
    print(i, end = ' ')

i = 1

while i <= 10:
    print(i, end = ' ')
    i = i + 1

i = 10
while i >= 1:
    print(i, end = ' ')
    i = i - 1

i = 1
while i <= 10:
    print(i)
    if i == 6:
        break
    i += 1

for i in range(1, 11):
    if i % 2 != 0:
        continue

    print(i, end=' ')

for i in range(1, 11):
    print(i, end = ' ')
    if i > 15:
        break
else:
    print(11)
