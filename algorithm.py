'''
k번째 약수
'''

n, k = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = ' ')