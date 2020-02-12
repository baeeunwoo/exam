'''
반복문을 이용한 문제풀이
 1) 1부터 N까지 홀수 출려
 2) 1부터 N까지의 합 구하기
 3) N의 약수출력하기

n = int(input())
for i in range(1, n + 1):
    print(i)
'''
# n = int(input())
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         continue
#     print(i, end = ' ')

# n = int(input())
# for i in range(1, n + 1):
#     if i % 2 == 1:
#         print(i)

# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print(sum)
#N의 약수출력하기

n = 20
for i in range(2, n + 1):
    if n % i == 0:
        print(i, end = ' ')

