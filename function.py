'''
함수만들기


def add(a, b):
    c = a + b
    print(c)

add(3, 2)
add(5, 10)

def add(a, b):
    c = a + b
    return c
print(add(3, 2))


def add(a, b):
    c = a + b
    d = a - b
    return c, d

print(add(5000, 6123012))
'''


def isPrime(x):  #x 지역변수
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for y in a:     #y 전역변수?   y는 a 하나하나 접근하는거 12, 13 ...
    if isPrime(y):
        print(y, end = ' ')






