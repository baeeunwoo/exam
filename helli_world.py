


def fibo(n):
    print("fibo:",n)
    if n <= 1:
        return n    #n = 0->0
    return fibo(n-2) + fibo(n-1)

print(fibo(7))
print(fibo(10))